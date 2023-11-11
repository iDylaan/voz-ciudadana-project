import axios from 'axios';

const authApi = axios.create({
    baseURL: 'https://vozciudadanaauth.fly.dev/api',
    headers: {
        'Content-Type': 'application/json'
    }
})

export default authApi;