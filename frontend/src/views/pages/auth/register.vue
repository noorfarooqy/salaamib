<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper login-body">
    <div class="login-wrapper">
      <div class="container">
        

        <div class="loginbox">
          <div class="login-right">
            <div class="login-right-wrap">
              <img class="img-fluid logo-dark mb-2" src="../../../assets/img/salaam_logo.png" alt="Logo" />
              <h1>Salaam Internet Banking</h1>
              <p class="account-subtitle">Register to Access </p>

              <div v-if="authStore.getErrors?.general" class="alert" :class="getAlertClass">
                {{ authStore.getErrors.general }}
              </div>

              <!-- Form -->
              <Form
                class="register"
                @submit="onSubmit"
                :validation-schema="validationSchema"
                v-slot="{ errors: formErrors }"
              >
                <!-- CIF Number -->
                <div class="form-group">
                  <label class="form-control-label">CIF Number</label>
                  <span class="text-danger">*</span>
                  <Field
                    name="cif"
                    type="text"
                    class="form-control mt-2"
                    :class="{ 'is-invalid': formErrors.cif || authStore.getErrors?.cif }"
                    placeholder="Enter your CIF number"
                  />
                  <div class="invalid-feedback" v-if="formErrors.cif || authStore.getErrors?.cif">
                    {{ formErrors.cif || authStore.getErrors?.cif }}
                  </div>
                </div>

                <!-- Password -->
                <div class="form-group mt-3">
                  <label class="form-control-label">Password</label>
                  <span class="text-danger">*</span>
                  <div class="pass-group">
                    <Field
                      name="password"
                      :type="showPassword ? 'text' : 'password'"
                      class="form-control mt-2"
                      :class="{ 'is-invalid': formErrors.password || authStore.getErrors?.password }"
                      placeholder="Enter your password"
                    />
                    <span 
                      class="fas toggle-password"
                      :class="showPassword ? 'fa-eye-slash' : 'fa-eye'"
                      @click="togglePasswordVisibility('password')"
                    ></span>
                  </div>
                  <div class="invalid-feedback" v-if="formErrors.password || authStore.getErrors?.password">
                    {{ formErrors.password || authStore.getErrors?.password }}
                  </div>
                </div>

                <!-- Confirm Password -->
                <div class="form-group mt-3">
                  <label class="form-control-label">Confirm Password</label>
                  <span class="text-danger">*</span>
                  <div class="pass-group">
                    <Field
                      name="confirmPassword"
                      :type="showConfirmPassword ? 'text' : 'password'"
                      class="form-control mt-2"
                      :class="{ 'is-invalid': formErrors.confirmPassword || authStore.getErrors?.confirmPassword }"
                      placeholder="Confirm your password"
                    />
                    <span 
                      class="fas toggle-password"
                      :class="showConfirmPassword ? 'fa-eye-slash' : 'fa-eye'"
                      @click="togglePasswordVisibility('confirmPassword')"
                    ></span>
                  </div>
                  <div class="invalid-feedback" v-if="formErrors.confirmPassword || authStore.getErrors?.confirmPassword">
                    {{ formErrors.confirmPassword || authStore.getErrors?.confirmPassword }}
                  </div>
                </div>

                <!-- Submit Button -->
                <div class="form-group mt-4">
                  <button
                    type="submit"
                    class="btn btn-primary w-100"
                    :disabled="loading"
                  >
                    <span v-if="loading" class="spinner-border spinner-border-sm me-2"></span>
                    {{ loading ? 'Registering...' : 'Register' }}
                  </button>
                </div>

                <!-- Login Link -->
                <div class="text-center mt-4">
                  <p>Already have an account? 
                    <router-link to="/">Login</router-link>
                  </p>
                </div>
              </Form>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- OTP Verification Modal -->
    <div v-if="showOtpModal" class="modal fade show" style="display: block">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Verify Your Account</h5>
            <button type="button" class="btn-close" @click="closeOtpModal"></button>
          </div>
          <div class="modal-body">
            <p class="mb-4">Please enter the verification code sent to your registered phone number.</p>
            
            <!-- Display OTP verification errors -->
            <div v-if="authStore.getErrors?.general" class="alert alert-danger mb-3">
              {{ authStore.getErrors.general }}
            </div>

            <Form @submit="handleOtpSubmit" :validation-schema="otpValidationSchema" v-slot="{ errors }">
              <div class="form-group">
                <label class="form-control-label">Verification Code</label>
                <Field
                  name="otp"
                  type="text"
                  class="form-control"
                  :class="{ 'is-invalid': errors.otp || authStore.getErrors?.otp }"
                  placeholder="Enter verification code"
                />
                <div class="invalid-feedback">{{ errors.otp || authStore.getErrors?.otp }}</div>
              </div>
              <div class="form-group mt-4">
                <button
                  type="submit"
                  class="btn btn-primary w-100"
                  :disabled="otpLoading"
                >
                  <span v-if="otpLoading" class="spinner-border spinner-border-sm me-2"></span>
                  {{ otpLoading ? 'Verifying...' : 'Verify' }}
                </button>
              </div>
            </Form>
            <div class="text-center mt-3">
              <p class="mb-0">
                Didn't receive the code? 
                <button 
                  class="btn btn-link p-0" 
                  @click="handleResendOtp"
                  :disabled="resendCooldown > 0 || resendLoading"
                >
                  {{ resendCooldown > 0 ? `Resend code in ${resendCooldown}s` : 'Resend code' }}
                </button>
              </p>
            </div>
          </div>
        </div>
      </div>
      <div class="modal-backdrop fade show"></div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../../../stores/auth'
import { Form, Field } from 'vee-validate'
import * as Yup from 'yup'

export default {
  components: {
    Form,
    Field
  },
  setup() {
    const router = useRouter()
    const authStore = useAuthStore()
    const showPassword = ref(false)
    const showConfirmPassword = ref(false)
    const loading = ref(false)
    const showOtpModal = ref(false)
    const otpLoading = ref(false)
    const resendLoading = ref(false)
    const registeredCif = ref('')
    const resendCooldown = ref(0)
    let cooldownInterval = null

    const validationSchema = Yup.object().shape({
      cif: Yup.string()
        .required('CIF number is required')
        .matches(/^\d+$/, 'CIF number must contain only digits'),
      password: Yup.string()
        .required('Password is required')
        .min(8, 'Password must be at least 8 characters')
        .matches(
          /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$/,
          'Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character'
        ),
      confirmPassword: Yup.string()
        .required('Please confirm your password')
        .oneOf([Yup.ref('password')], 'Passwords must match')
    })

    const otpValidationSchema = Yup.object().shape({
      otp: Yup.string()
        .required('OTP is required')
        .matches(/^\d{6}$/, 'OTP must be 6 digits')
    })

    const getAlertClass = computed(() => {
      const errorMessage = authStore.getErrors?.general || '';
      if (errorMessage.includes('Too many failed attempts')) {
        return 'alert-danger';
      }
      if (errorMessage.includes('attempts remaining')) {
        return 'alert-warning';
      }
      return 'alert-danger';
    });

    const startResendCooldown = () => {
      resendCooldown.value = 60
      cooldownInterval = setInterval(() => {
        if (resendCooldown.value > 0) {
          resendCooldown.value--
        } else {
          clearInterval(cooldownInterval)
        }
      }, 1000)
    }

    const onSubmit = async (values) => {
      try {
        loading.value = true
        // Convert data to form data format
        const formData = new URLSearchParams()
        formData.append('cif_number', values.cif)
        formData.append('password', values.password)

        await authStore.register({
          formData,
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })
        registeredCif.value = values.cif
        showOtpModal.value = true
        startResendCooldown()
      } catch (error) {
        console.error('Registration error:', error)
      } finally {
        loading.value = false
      }
    }

    const handleOtpSubmit = async (values) => {
      try {
        otpLoading.value = true
        authStore.clearErrors() // Clear previous errors
        await authStore.verifyOTP({
          cif_number: registeredCif.value,
          otp: values.otp
        })
        showOtpModal.value = false
        router.push('/login')
      } catch (error) {
        console.error('OTP verification error:', error)
      } finally {
        otpLoading.value = false
      }
    }

    const handleResendOtp = async () => {
      if (resendCooldown.value > 0) return;
      
      try {
        resendLoading.value = true
        await authStore.resendOTP({
          cif_number: registeredCif.value
        })
        startResendCooldown()
      } catch (error) {
        console.error('Resend OTP error:', error)
      } finally {
        resendLoading.value = false
      }
    }

    const togglePasswordVisibility = (field) => {
      if (field === 'password') {
        showPassword.value = !showPassword.value
      } else {
        showConfirmPassword.value = !showConfirmPassword.value
      }
    }

    const closeOtpModal = () => {
      showOtpModal.value = false
      router.push('/login')
    }

    onUnmounted(() => {
      if (cooldownInterval) {
        clearInterval(cooldownInterval)
      }
    })

    return {
      showPassword,
      showConfirmPassword,
      loading,
      showOtpModal,
      otpLoading,
      resendLoading,
      registeredCif,
      resendCooldown,
      validationSchema,
      otpValidationSchema,
      errors: {},
      onSubmit,
      handleOtpSubmit,
      handleResendOtp,
      togglePasswordVisibility,
      closeOtpModal,
      authStore,
      getAlertClass
    }
  }
}
</script>

<style scoped>
.pass-group {
  position: relative;
}

.toggle-password {
  position: absolute;
  right: 15px;
  top: 50%;
  transform: translateY(-50%);
  cursor: pointer;
  color: #757575;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1050;
}

.modal-dialog {
  position: relative;
  width: 100%;
  max-width: 500px;
  margin: 1.75rem auto;
  z-index: 1055;
}

.modal-content {
  position: relative;
  background-color: #fff;
  border-radius: 0.3rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
  z-index: 1060;
}

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1040;
}

.disabled {
  pointer-events: none;
  opacity: 0.6;
}

.alert {
  padding: 0.75rem 1.25rem;
  margin-bottom: 1rem;
  border: 1px solid transparent;
  border-radius: 0.25rem;
}

.alert-warning {
  color: #856404;
  background-color: #fff3cd;
  border-color: #ffeeba;
}

.alert-danger {
  color: #721c24;
  background-color: #f8d7da;
  border-color: #f5c6cb;
}

.invalid-feedback {
  display: block;
  width: 100%;
  margin-top: 0.25rem;
  font-size: 0.875em;
  color: #dc3545;
}

.btn-close {
  padding: 0.5rem 0.5rem;
  margin: -0.5rem -0.5rem -0.5rem auto;
}

.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  border-bottom: 1px solid #dee2e6;
}

.modal-body {
  padding: 1rem;
}
</style>
