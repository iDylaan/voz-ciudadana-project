import { reportApi, privateReportApi } from '@/api/reports_api.js';
import router from '@/router';

export async function getReports({ commit }) {
    commit('cleanReports');
    try {
        const response = await reportApi.get('/reports');

        if (response.status !== 200) {
            throw new Error(response.statusText); 
        }
        const result = response.data;
        if (result.status === "OK") {
            commit('setReports', result.data);
        } else {
            throw new Error("Error inesperado al obtener los reportes, intenta nuevamente más tarde. 🙁");
        }

    } catch (error) {
        throw new Error(error);
    }
}

export async function getUserReports({ commit }, payload) {
    commit('cleanUserReports');
    try {
        const response = await reportApi.get(`/user_reports/${payload.user_id}`);

        if (response.status !== 200) {
            throw new Error(response.statusText); 
        }
        const result = response.data;
        if (result.status === "OK") {
            commit('setReports', data);
        } else {
            throw new Error("Error inesperado al obtener los reportes, intenta nuevamente más tarde. 🙁");
        }

    } catch (error) {
        throw new Error(error);
    }
}