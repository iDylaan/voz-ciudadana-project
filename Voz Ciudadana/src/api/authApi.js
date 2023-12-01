import axios from 'axios'

export const authApi = axios.create({
    baseURL: 'https://voz-ciudadana-auth.fly.dev'
})

export const authApiJWT = axios.create({
    baseURL: 'https://voz-ciudadana-auth.fly.dev',
    headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
    }
})