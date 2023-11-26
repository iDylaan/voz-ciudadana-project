import axios from 'axios'

export const authApi = axios.create({
    baseURL: 'https://voz-ciudadana-project-production.up.railway.app'
})

export const authApiJWT = axios.create({
    baseURL: 'https://voz-ciudadana-project-production.up.railway.app',
    headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
    }
})