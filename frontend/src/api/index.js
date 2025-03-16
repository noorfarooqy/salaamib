import axios from 'axios'

// Configure axios base URL
export const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL || 'http://127.0.0.1:8000',
  headers: {
    'Content-Type': 'application/json'
  }
})

// Add request interceptor
api.interceptors.request.use(
  (config) => {
    // You can add common request handling here
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Add response interceptor
api.interceptors.response.use(
  (response) => {
    return response
  },
  (error) => {
    // Handle common error responses here
    if (error.response?.status === 401) {
      // Handle unauthorized access
      localStorage.removeItem('token')
      sessionStorage.removeItem('token')
    }
    return Promise.reject(error)
  }
)

export default api 