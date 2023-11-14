import axios from 'axios'

const authApi = axios.create({
    baseURL: 'https://voz-ciudadana-project-production.up.railway.app'
})

export default authApi