<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper login-body">
    <div class="login-wrapper">
      <div class="loginbox">
        <div class="login-right">
          <div class="login-right-wrap">
            <div class="container">
              <img class="img-fluid logo-dark mb-2 logo-color" src="../../../assets/img/salaam_logo.png" alt="Logo" />
              <img class="img-fluid logo-light mb-2" src="../../../assets/img/salaam_logo.png" alt="Logo" />
              <h1>Salaam Internet Banking</h1>
              <p class="account-subtitle">Access to our dashboard</p>

              <!-- Display general errors -->
              <div v-if="authStore.getErrors?.general" :class="['alert', getAlertClass]" role="alert">
                {{ authStore.getErrors.general }}
                <div v-if="showAttemptsWarning" class="mt-2 text-warning">
                  <i class="fas fa-exclamation-triangle me-2"></i>
                  Warning: Multiple failed attempts will lock your account for 30 minutes.
                </div>
              </div>

              <!-- Login Form -->
              <Form v-if="!show2FA" @submit="onSubmit" :validation-schema="validationSchema">
                <div class="input-block mb-3">
                  <label class="form-control-label">CIF Number</label>
                  <Field v-slot="{ field, errors: fieldErrors }" name="username" type="text">
                    <input
                      v-bind="field"
                      class="form-control"
                      :class="{ 'is-invalid': fieldErrors.length > 0 || authStore.getErrors?.username }"
                      placeholder="Enter your CIF number"
                    />
                    <div class="invalid-feedback">
                      {{ fieldErrors[0] || authStore.getErrors?.username }}
                    </div>
                  </Field>
                </div>
                <div class="input-block mb-3">
                  <label class="form-control-label">Password</label>
                  <div class="pass-group">
                    <Field v-slot="{ field, errors: fieldErrors }" name="password">
                      <input
                        v-bind="field"
                        :type="showPassword ? 'text' : 'password'"
                        class="form-control pass-input mt-2"
                        :class="{ 'is-invalid': fieldErrors.length > 0 || authStore.getErrors?.password }"
                        placeholder="Enter your password"
                      />
                      <div class="invalid-feedback">
                        {{ fieldErrors[0] || authStore.getErrors?.password }}
                      </div>
                    </Field>
                    <span @click="togglePasswordVisibility" class="toggle-password">
                      <i :class="{
                        'fas fa-eye': showPassword,
                        'fas fa-eye-slash': !showPassword,
                      }"></i>
                    </span>
                  </div>
                </div>
                <div class="input-block mb-3">
                  <div class="row">
                    <div class="col-6">
                      <div class="form-check custom-checkbox">
                        <Field type="checkbox" class="form-check-input" id="rememberMe" name="rememberMe" v-model="rememberMe" />
                        <label class="custom-control-label" for="rememberMe">Remember me</label>
                      </div>
                    </div>
                    <div class="col-6 text-end">
                      <router-link class="forgot-link" to="forgot-password">Forgot Password ?</router-link>
                    </div>
                  </div>
                </div>
                <button class="btn btn-lg btn-primary w-100" type="submit" :disabled="loading">
                  <span v-if="loading" class="spinner-border spinner-border-sm me-2"></span>
                  {{ loading ? 'Signing in...' : 'Sign in' }}
                </button>
              </Form>

              <!-- 2FA Form -->
              <div v-if="show2FA" class="login-form">
                <div class="login-header">
                  <h3>Two-Factor Authentication</h3>
                  <p>Please enter the verification code sent to your phone</p>
                </div>
                

                <Form @submit="verify2FA" :validation-schema="otpValidationSchema">
                  <div class="form-group">
                    <label class="form-control-label">Verification Code</label>
                    <Field name="otp" placeholder="Enter your verification code" type="text" class="form-control" :class="{ 'is-invalid': authStore.getErrors?.otp }" />
                    <div class="invalid-feedback" v-if="authStore.getErrors?.otp">
                      {{ authStore.getErrors.otp }}
                    </div>
                  </div>

                  <div class="form-group mt-4">
                    <button type="submit" class="btn btn-primary btn-block" :disabled="loading">
                      {{ loading ? 'Verifying...' : 'Verify' }}
                    </button>
                  </div>

                  <div class="form-group text-center">
                    <button 
                      type="button" 
                      class="btn btn-link" 
                      @click="resendOTP" 
                      :disabled="resendCooldown > 0 || loading"
                    >
                      {{ resendCooldown > 0 ? `Resend code in ${resendCooldown}s` : 'Resend code' }}
                    </button>
                  </div>
                </Form>
              </div>

              <div class="login-or">
                <span class="or-line"></span>
                <span class="span-or">or</span>
              </div>
              <div class="text-center dont-have">
                Don't have an account yet?
                <router-link to="register">Register</router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Main Wrapper -->

  <!-- Verification Modal -->
  <div v-if="showVerificationModal" class="modal">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Account Verification</h5>
          <button type="button" class="btn-close" @click="closeVerificationModal"></button>
        </div>
        <div class="modal-body">
          <!-- Show error alert if there are errors -->
          <div v-if="authStore.getErrors" :class="['alert', getAlertClass]" role="alert">
            {{ authStore.getErrors.general || Object.values(authStore.getErrors)[0] }}
          </div>

          <Form @submit="handleVerificationSubmit" :validation-schema="otpValidationSchema">
            <div class="form-group">
              <label class="form-control-label">Verification Code</label>
              <Field name="otp" type="text" placeholder="Enter your verification code" class="form-control" :class="{ 'is-invalid': authStore.getErrors?.otp }" />
              <div class="invalid-feedback" v-if="authStore.getErrors?.otp">
                {{ authStore.getErrors.otp }}
              </div>
            </div>

            <div class="form-group mt-4">
              <button type="submit" class="btn btn-primary btn-block" :disabled="verificationLoading">
                {{ verificationLoading ? 'Verifying...' : 'Verify' }}
              </button>
            </div>

            <div class="form-group text-center">
              <button 
                type="button" 
                class="btn btn-link" 
                :disabled="resendCooldown > 0 || verificationLoading"
              >
                {{ resendCooldown > 0 ? `Resend code in ${resendCooldown}s` : 'Resend code' }}
              </button>
            </div>
          </Form>
        </div>
      </div>
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
    const loading = ref(false)
    const rememberMe = ref(false)
    const show2FA = ref(false)
    const cifNumber = ref('')
    const failedAttempts = ref(0)
    const resendCooldown = ref(0)
    let cooldownInterval = null
    const showVerificationModal = ref(false)
    const verificationLoading = ref(false)
    const registeredCif = ref('')
    const storedPassword = ref('')
    const storedRememberMe = ref(false)

    // Common validation schema for OTP
    const otpValidationSchema = {
      otp: Yup.string()
        .required('Verification code is required')
        .matches(/^\d+$/, 'Verification code must contain only digits')
        .length(6, 'Verification code must be 6 digits')
    }

    // Login form validation schema
    const validationSchema = {
      username: Yup.string()
        .required('CIF number is required')
        .matches(/^\d+$/, 'CIF number must contain only digits'),
      password: Yup.string()
        .required('Password is required')
    }

    const showAttemptsWarning = computed(() => {
      const errorMessage = authStore.getErrors?.general || '';
      return errorMessage.includes('attempts remaining') || errorMessage.includes('Account is locked');
    });

    const getAlertClass = computed(() => {
      const errorMessage = authStore.getErrors?.general || '';
      if (errorMessage.includes('Account is locked')) {
        return 'alert-danger';
      }
      if (errorMessage.includes('attempts remaining')) {
        return 'alert-warning';
      }
      return 'alert-danger';
    });

    // Common function to handle OTP verification
    const handleOTPVerification = async (values, type) => {
      const isVerification = type === 'verification'
      const loadingRef = isVerification ? verificationLoading : loading
      
      try {
        loadingRef.value = true
        authStore.clearErrors()

        if (isVerification) {
          await authStore.verifyOTP({
            cif_number: registeredCif.value,
            otp: values.otp
          })
          showVerificationModal.value = false
          await onSubmit({
            username: registeredCif.value,
            password: storedPassword.value,
            rememberMe: storedRememberMe.value
          })
        } else {
          await authStore.verify2FA({
            cif_number: cifNumber.value,
            otp: values.otp
          })
        }
        
        router.push('/dashboard')
      } catch (error) {
        console.error(`${type} verification error:`, error)
      } finally {
        loadingRef.value = false
      }
    }

    // Common function to handle OTP resend
    const handleOTPResend = async (type) => {
      try {
        if (resendCooldown.value > 0) return
        
        const isVerification = type === 'verification'
        const loadingRef = isVerification ? verificationLoading : loading
        
        loadingRef.value = true
        authStore.clearErrors()

        if (isVerification) {
          await authStore.resendOTP({
            cif_number: registeredCif.value
          })
        } else {
          await authStore.resend2FAOTP({
            cif_number: cifNumber.value
          })
        }
        
        startResendCooldown()
      } catch (error) {
        console.error(`Resend ${type} error:`, error)
      } finally {
        loadingRef.value = false
      }
    }

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
        const response = await authStore.login({
          cif: values.username,
          password: values.password,
          rememberMe: values.rememberMe
        })

        if (response.requires_2fa) {
          cifNumber.value = response.cif_number
          show2FA.value = true
          startResendCooldown()
        } else if (response.requires_verification) {
          registeredCif.value = response.cif_number
          storedPassword.value = values.password
          storedRememberMe.value = values.rememberMe
          showVerificationModal.value = true
          startResendCooldown()
        } else {
          router.push('/dashboard')
        }
      } catch (error) {
        console.error('Login error:', error)
      } finally {
        loading.value = false
      }
    }

    const togglePasswordVisibility = () => {
      showPassword.value = !showPassword.value
    }

    const closeVerificationModal = () => {
      showVerificationModal.value = false
      authStore.clearErrors()
    }

    // Cleanup on component unmount
    onUnmounted(() => {
      if (cooldownInterval) {
        clearInterval(cooldownInterval)
      }
    })

    return {
      validationSchema,
      otpValidationSchema,
      showPassword,
      loading,
      rememberMe,
      show2FA,
      onSubmit,
      verify2FA: (values) => handleOTPVerification(values, '2fa'),
      handleVerificationSubmit: (values) => handleOTPVerification(values, 'verification'),
      togglePasswordVisibility,
      authStore,
      showAttemptsWarning,
      getAlertClass,
      resendOTP: () => handleOTPResend('2fa'),
      handleResendVerification: () => handleOTPResend('verification'),
      resendCooldown,
      showVerificationModal,
      verificationLoading,
      closeVerificationModal,
      registeredCif,
      cifNumber
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

.alert {
  margin-bottom: 1rem;
  padding: 1rem;
  border-radius: 0.375rem;
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

.text-warning {
  color: #856404 !important;
  font-size: 0.875rem;
}

.fa-exclamation-triangle {
  color: #856404;
}

.btn-link {
  text-decoration: none;
}
.btn-link:hover {
  text-decoration: underline;
}

/* Modal Styles */
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
  z-index: 9999;
}

.modal-dialog {
  position: relative;
  width: 100%;
  max-width: 500px;
  margin: 1.75rem auto;
  pointer-events: auto;
  z-index: 10000;
}

.modal-content {
  position: relative;
  background-color: #fff;
  border-radius: 0.3rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
  pointer-events: auto;
  z-index: 10001;
}

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 9998;
}

.modal-header {
  border-bottom: 1px solid #dee2e6;
  padding: 1rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-body {
  padding: 1rem;
}

.btn-close {
  background: transparent;
  border: 0;
  font-size: 1.5rem;
  padding: 0.5rem;
  margin: -0.5rem -0.5rem -0.5rem auto;
  cursor: pointer;
}

.invalid-feedback {
  display: block;
  width: 100%;
  margin-top: 0.25rem;
  font-size: 0.875em;
  color: #dc3545;
}
</style>
