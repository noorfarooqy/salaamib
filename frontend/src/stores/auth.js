import { defineStore } from 'pinia'
import { api } from '../api'
import { encryptData, decryptData } from '../utils/encryption'

// Helper function to format validation errors
const formatValidationErrors = (detail) => {
  if (Array.isArray(detail)) {
    const errors = {}
    detail.forEach(error => {
      const field = error.loc[error.loc.length - 1]
      errors[field] = error.msg
    })
    return errors
  }
  return { general: detail }
}

// Helper function to convert object to form data
const objectToFormData = (obj) => {
  const formData = new URLSearchParams()
  Object.entries(obj).forEach(([key, value]) => {
    formData.append(key, value)
  })
  return formData
}

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: null,
    user: null,
    errors: null
  }),

  getters: {
    isAuthenticated: (state) => !!state.token,
    getUser: (state) => state.user,
    getErrors: (state) => state.errors
  },

  actions: {
    clearErrors() {
      this.errors = null
    },

    initialize() {
      try {
        const token = localStorage.getItem('token') || sessionStorage.getItem('token')
        const encryptedUserData = localStorage.getItem('user') || sessionStorage.getItem('user')
        
        if (token && encryptedUserData) {
          try {
            const userData = decryptData(encryptedUserData)
            if (userData) {
              this.token = token
              this.user = userData
              api.defaults.headers.common['Authorization'] = `Bearer ${token}`
            } else {
              this.clearAuthData()
            }
          } catch (e) {
            console.warn('Failed to decrypt stored user data:', e)
            this.clearAuthData()
          }
        } else {
          this.clearAuthData()
        }
      } catch (e) {
        console.warn('Error during auth initialization:', e)
        this.clearAuthData()
      }
    },

    clearAuthData() {
      this.token = null
      this.user = null
      this.errors = null
      delete api.defaults.headers.common['Authorization']
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      sessionStorage.removeItem('token')
      sessionStorage.removeItem('user')
    },

    async login(credentials) {
      try {
        this.clearErrors()
        
        // Convert credentials to form data
        const formData = objectToFormData({
          username: credentials.cif,
          password: credentials.password
        })

        const response = await api.post('/api/v1/auth/login', formData, {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })

        // If 2FA is required, return the response
        if (response.data.requires_2fa) {
          return response.data
        }

        // If user is not verified (403 error), this will be caught in the catch block
        const { access_token, user } = response.data
        this.setAuthData(access_token, user, credentials.rememberMe)
        return response.data
      } catch (error) {
        if (error.response?.status === 403) {
          // Return special object for unverified users
          return {
            requires_verification: true,
            cif_number: credentials.cif,
            message: error.response.data.detail
          }
        }
        this.handleError(error)
        throw this.errors
      }
    },

    async verify2FA(data) {
      try {
        this.clearErrors()
        
        // Convert data to form data
        const formData = objectToFormData({
          cif_number: data.cif_number,
          otp: data.otp
        })

        const response = await api.post('/api/v1/auth/verify-2fa', formData, {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })

        const { access_token, user } = response.data
        this.setAuthData(access_token, user, true) // Use stored rememberMe preference
        return response.data
      } catch (error) {
        this.handleError(error)
        throw this.errors
      }
    },

    setAuthData(token, user, rememberMe) {
      // Encrypt user data before storing
      const encryptedUserData = encryptData(user)
      
      // Store in either localStorage or sessionStorage based on rememberMe
      const storage = rememberMe ? localStorage : sessionStorage
      storage.setItem('token', token)
      storage.setItem('user', encryptedUserData)
      
      this.token = token
      this.user = user
      api.defaults.headers.common['Authorization'] = `Bearer ${token}`
    },

    handleError(error) {
      if (error.response) {
        if (error.response.status === 422) {
          this.errors = formatValidationErrors(error.response.data.detail)
        } else {
          this.errors = {
            general: error.response.data.detail || 'An error occurred'
          }
        }
      } else if (error.request) {
        this.errors = {
          general: 'Network error. Please check your connection.'
        }
      } else {
        this.errors = {
          general: error.message || 'An unexpected error occurred'
        }
      }
    },

    async register(data) {
      try {
        this.clearErrors()
        const response = await api.post('/api/v1/auth/register', data.formData, {
          headers: data.headers
        })
        return response.data
      } catch (error) {
        if (error.response) {
          if (error.response.status === 422) {
            this.errors = formatValidationErrors(error.response.data.detail)
          } else {
            this.errors = {
              general: error.response.data.detail || 'Registration failed'
            }
          }
        } else if (error.request) {
          this.errors = {
            general: 'Network error. Please check your connection.'
          }
        } else {
          this.errors = {
            general: error.message || 'An unexpected error occurred'
          }
        }
        throw this.errors
      }
    },

    async verifyOTP(data) {
      try {
        this.clearErrors()
        // Convert data to form data format
        const formData = JSON.stringify({
          cif_number: data.cif_number,
          otp: data.otp
        })

        const response = await api.post('/api/v1/auth/verify', formData, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        return response.data
      } catch (error) {
        if (error.response) {
          if (error.response.status === 422) {
            this.errors = formatValidationErrors(error.response.data.detail)
          } else {
            this.errors = {
              general: error.response.data.detail || 'OTP verification failed'
            }
          }
        } else if (error.request) {
          this.errors = {
            general: 'Network error. Please check your connection.'
          }
        } else {
          this.errors = {
            general: error.message || 'An unexpected error occurred'
          }
        }
        throw this.errors
      }
    },

    async resendOTP(data) {
      try {
        this.clearErrors()
        // Convert data to form data format
        const formData = objectToFormData({
          cif_number: data.cif_number
        })

        const response = await api.post('/api/v1/auth/resend-otp', formData, {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })
        return response.data
      } catch (error) {
        if (error.response) {
          if (error.response.status === 422) {
            this.errors = formatValidationErrors(error.response.data.detail)
          } else {
            this.errors = {
              general: error.response.data.detail || 'Failed to resend OTP'
            }
          }
        } else if (error.request) {
          this.errors = {
            general: 'Network error. Please check your connection.'
          }
        } else {
          this.errors = {
            general: error.message || 'An unexpected error occurred'
          }
        }
        throw this.errors
      }
    },

    async resend2FAOTP(data) {
      try {
        this.clearErrors()
        // Convert data to form data
        const formData = objectToFormData({
          cif_number: data.cif_number
        })

        const response = await api.post('/api/v1/auth/resend-2fa', formData, {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })
        return response.data
      } catch (error) {
        this.handleError(error)
        throw this.errors
      }
    },

    logout() {
      this.clearAuthData()
    },

    async forgotPassword(data) {
      try {
        this.clearErrors()
        const formData = JSON.stringify(data)
        const response = await api.post('/api/v1/auth/forgot-password', formData)
        return response.data
      } catch (error) {
        this.handleError(error)
        throw error
      }
    },

    async resetPassword(data) {
      try {
        this.clearErrors()
        const formData = JSON.stringify(data)
        const response = await api.post('/api/v1/auth/reset-password', formData)
        return response.data
      } catch (error) {
        this.handleError(error)
        throw error
      }
    }
  }
}) 