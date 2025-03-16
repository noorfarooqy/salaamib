<template>
  <div class="main-wrapper login-body">
    <div class="login-wrapper">
      <div class="loginbox">
        <div class="login-right">
          <div class="login-right-wrap">
            <div class="container">
              <img class="img-fluid logo-dark mb-2 logo-color" src="../../../assets/img/salaam_logo.png" alt="Logo" />
              <img class="img-fluid logo-light mb-2" src="../../../assets/img/salaam_logo.png" alt="Logo" />
              <h1>Forgot Password</h1>
              <p class="account-subtitle">Enter your CIF number to reset your password</p>

              <!-- Display general errors -->
              <div v-if="authStore.getErrors?.general" class="alert alert-danger" role="alert">
                {{ authStore.getErrors.general }}
              </div>

              <!-- Step 1: CIF Input Form -->
              <Form v-if="!showResetForm" @submit="onSubmitCIF" :validation-schema="cifValidationSchema">
                <div class="input-block mb-3">
                  <label class="form-control-label">CIF Number</label>
                  <Field v-slot="{ field, errors: fieldErrors }" name="cif_number" type="text">
                    <input
                      v-bind="field"
                      class="form-control"
                      :class="{ 'is-invalid': fieldErrors.length > 0 || authStore.getErrors?.cif_number }"
                      placeholder="Enter your CIF number"
                    />
                    <div class="invalid-feedback">
                      {{ fieldErrors[0] || authStore.getErrors?.cif_number }}
                    </div>
                  </Field>
                </div>
                <button class="btn btn-lg btn-primary w-100" type="submit" :disabled="loading">
                  <span v-if="loading" class="spinner-border spinner-border-sm me-2"></span>
                  {{ loading ? 'Processing...' : 'Continue' }}
                </button>
              </Form>

              <!-- Step 2: Reset Password Form -->
              <Form v-else @submit="onSubmitReset" :validation-schema="resetValidationSchema">
                <div class="input-block mb-3">
                  <label class="form-control-label">Verification Code</label>
                  <Field v-slot="{ field, errors: fieldErrors }" name="otp" type="text">
                    <input
                      v-bind="field"
                      class="form-control"
                      :class="{ 'is-invalid': fieldErrors.length > 0 || authStore.getErrors?.otp }"
                      placeholder="Enter verification code"
                    />
                    <div class="invalid-feedback">
                      {{ fieldErrors[0] || authStore.getErrors?.otp }}
                    </div>
                  </Field>
                </div>

                <div class="input-block mb-3">
                  <label class="form-control-label">New Password</label>
                  <div class="pass-group">
                    <Field v-slot="{ field, errors: fieldErrors }" name="new_password">
                      <input
                        v-bind="field"
                        :type="showPassword ? 'text' : 'password'"
                        class="form-control pass-input"
                        :class="{ 'is-invalid': fieldErrors.length > 0 || authStore.getErrors?.new_password }"
                        placeholder="Enter new password"
                      />
                      <div class="invalid-feedback">
                        {{ fieldErrors[0] || authStore.getErrors?.new_password }}
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
                  <label class="form-control-label">Confirm Password</label>
                  <div class="pass-group">
                    <Field v-slot="{ field, errors: fieldErrors }" name="confirm_password">
                      <input
                        v-bind="field"
                        :type="showPassword ? 'text' : 'password'"
                        class="form-control pass-input"
                        :class="{ 'is-invalid': fieldErrors.length > 0 }"
                        placeholder="Confirm new password"
                      />
                      <div class="invalid-feedback">
                        {{ fieldErrors[0] }}
                      </div>
                    </Field>
                  </div>
                </div>

                <div class="form-group text-center mb-3">
                  <button 
                    type="button" 
                    class="btn btn-link" 
                    @click="resendOTP" 
                    :disabled="resendCooldown > 0 || loading"
                  >
                    {{ resendCooldown > 0 ? `Resend code in ${resendCooldown}s` : 'Resend code' }}
                  </button>
                </div>

                <button class="btn btn-lg btn-primary w-100" type="submit" :disabled="loading">
                  <span v-if="loading" class="spinner-border spinner-border-sm me-2"></span>
                  {{ loading ? 'Resetting Password...' : 'Reset Password' }}
                </button>
              </Form>

              <div class="login-or">
                <span class="or-line"></span>
                <span class="span-or">or</span>
              </div>
              <div class="text-center dont-have">
                Remember your password? <router-link to="/login">Login</router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onUnmounted } from 'vue'
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
    const loading = ref(false)
    const showPassword = ref(false)
    const showResetForm = ref(false)
    const resendCooldown = ref(0)
    const cifNumber = ref('')
    let cooldownInterval = null

    // Validation schema for CIF input
    const cifValidationSchema = {
      cif_number: Yup.string()
        .required('CIF number is required')
        .matches(/^\d+$/, 'CIF number must contain only digits')
    }

    // Validation schema for password reset
    const resetValidationSchema = {
      otp: Yup.string()
        .required('Verification code is required')
        .matches(/^\d+$/, 'Verification code must contain only digits')
        .length(6, 'Verification code must be 6 digits'),
      new_password: Yup.string()
        .required('New password is required')
        .min(8, 'Password must be at least 8 characters')
        .matches(
          /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$/,
          'Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character'
        ),
      confirm_password: Yup.string()
        .required('Please confirm your password')
        .oneOf([Yup.ref('new_password')], 'Passwords must match')
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

    const onSubmitCIF = async (values) => {
      try {
        loading.value = true
        await authStore.forgotPassword({
          cif_number: values.cif_number
        })
        cifNumber.value = values.cif_number
        showResetForm.value = true
        startResendCooldown()
      } catch (error) {
        console.error('Forgot password error:', error)
      } finally {
        loading.value = false
      }
    }

    const onSubmitReset = async (values) => {
      try {
        loading.value = true
        await authStore.resetPassword({
          cif_number: cifNumber.value,
          otp: values.otp,
          new_password: values.new_password
        })
        router.push('/login')
      } catch (error) {
        console.error('Reset password error:', error)
      } finally {
        loading.value = false
      }
    }

    const resendOTP = async () => {
      try {
        if (resendCooldown.value > 0) return
        loading.value = true
        await authStore.forgotPassword({
          cif_number: cifNumber.value
        })
        startResendCooldown()
      } catch (error) {
        console.error('Resend OTP error:', error)
      } finally {
        loading.value = false
      }
    }

    const togglePasswordVisibility = () => {
      showPassword.value = !showPassword.value
    }

    // Cleanup on component unmount
    onUnmounted(() => {
      if (cooldownInterval) {
        clearInterval(cooldownInterval)
      }
    })

    return {
      loading,
      showPassword,
      showResetForm,
      resendCooldown,
      cifValidationSchema,
      resetValidationSchema,
      onSubmitCIF,
      onSubmitReset,
      resendOTP,
      togglePasswordVisibility,
      authStore
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

.btn-link {
  text-decoration: none;
}

.btn-link:hover {
  text-decoration: underline;
}
</style>
