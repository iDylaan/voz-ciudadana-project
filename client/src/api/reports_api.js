import axios from 'axios';

export const reportApi = axios.create({
    baseURL: 'https://voz-ciudadana-reports.fly.dev',
    headers: {
        'Content-Type': 'application/json'
    }
})

export const privateReportApi = axios.create({
    baseURL: 'https://voz-ciudadana-reports.fly.dev',
    headers: {
        'Content-Type': 'application/json'
    }
})

privateReportApi.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');

    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
}, (error) => {
    return Promise.reject(error);
});