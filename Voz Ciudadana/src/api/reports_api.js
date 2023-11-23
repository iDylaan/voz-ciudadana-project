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
        'Content-Type': 'application/json',
        Authorization: `Bearer ${localStorage.getItem('token')}`
    }
})