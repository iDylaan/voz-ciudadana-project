import { privateReportApi, reportApi } from "@/api/reports_api.js";

/**
 * This function is used to get all the reports from the backend.
 * 
 * @param {Object} commit - The commit method is a function that allows us to modify the state.
 * 
 * @returns {void}
 */
export async function getReports({ commit }) {
    commit('cleanReports'); // This function is used to clean the reports array in the state.

    try {
        const response = await reportApi.get('/reports'); // This line makes a GET request to the /reports endpoint of the backend.

        if (response.status !== 200) {
            throw new Error(response.statusText); // If the response status is not 200 (OK), an error is thrown with the response status text.
        }

        const result = response.data; // The response data is assigned to the result variable.

        if (result.status === "OK") {
            commit('setReports', result.data); // If the status of the response data is "OK", the setReports function is called with the data from the response.
        } else {
            throw new Error("Error inesperado al obtener los reportes, intenta nuevamente más tarde. 🙁"); // If the status is not "OK", an error is thrown with the specified message.
        }

    } catch (error) {
        throw new Error(error); // The error is thrown again.
    }
}

/**
 * This function is used to get the reports of a specific user from the backend.
 * 
 * @param {Object} commit - The commit method is a function that allows us to modify the state.
 * @param {Object} payload - The payload object contains the user ID.
 * 
 * @returns {void}
 */
export async function getUserReports({ commit }, user_id) {
    commit('cleanUserReports'); // This function is used to clean the userReports array in the state.

    try {
        const response = await privateReportApi.get(`/user_reports/${user_id}`); // This line makes a GET request to the /user_reports/:user_id endpoint of the backend, where :user_id is the user ID passed in the payload.

        if (response.status !== 200) {
            throw new Error(response.statusText); // If the response status is not 200 (OK), an error is thrown with the response status text.
        }
        const result = response.data; // The response data is assigned to the result variable.

        if (result.success) {
            const reports = result.data? result.data : [];
            commit('setReports', reports); // If the status of the response data is "OK", the setReports function is called with the data from the response.
        } else {
            throw new Error("Error inesperado al obtener los reportes, intenta nuevamente más tarde. 🙁"); // If the status is not "OK", an error is thrown with the specified message.
        }

    } catch (error) {
        throw new Error(error); // The error is thrown again.
    }
}

/**
 * This function is used to get the report categories from the private backend.
 * 
 * @param {Object} commit - The commit method is a function that allows us to modify the state.
 * @param {Object} payload - This parameter is not used in this function.
 * 
 * @returns {void}
 */
export async function getReportCategories({ commit }, payload) {
    commit('cleanReportsCategories'); // This function is used to clean the reportCategories array in the state.

    try {
        const response = await privateReportApi.get(`/categories`); // This line makes a GET request to the /categories endpoint of the private backend.

        if (response.status !== 200) {
            throw new Error(response.statusText); // If the response status is not 200 (OK), an error is thrown with the response status text.
        }

        const result = response.data; // The response data is assigned to the result variable.

        if (result.status === "OK") {
            commit('setReportsCategories', result.data); // If the status of the response data is "OK", the setReportsCategories function is called with the data from the response.
        } else {
            throw new Error("Error inesperado al obtener las categorías, intenta nuevamente más tarde. 🙁"); // If the status is not "OK", an error is thrown with the specified message.
        }
    } catch (error) {
        throw new Error(error); // The error is thrown again.
    }
}

/**
 * This function is used to get the report categories from the private backend.
 *  
 * @param {Object} commit - The commit method is a function that allows us to modify
 *  the state.
 * @param {Object} payload - This parameter is not used in this function.
 *  
 * @returns {void}
 */
export async function createReport({ commit }, report) {
    try {
        const response = await privateReportApi.post('/reports', report); // This line makes a POST request to the /reports endpoint of the private backend.
        if (response.status !== 200) {
            throw new Error(response.statusText); // If the response status is not 200 (OK), an error is thrown with the response status text.
        }

        const result = response.data; // The response data is assigned to the result variable.

        if (result.status === "OK") {
            return true; // If the status of the response data is "OK", the setReportsCategories function is called with the data from the response.
        } else {
            throw new Error("No se pudo crear el reporte, intenta nuevamente más tarde. 🙁"); // If the status is not "OK", an error is thrown with the specified message.
        }
    } catch (error) {
        throw new Error(error); // The error is thrown again.
    }
}

export async function getPendingReports({ commit }) {
    try {
        const response = await reportApi.get('/pending_reports'); // This line makes a GET request to the /pending_reports
        if (response.status !== 200) {
            throw new Error(response.statusText); // If the response status is not 200 (OK
        }
        const result = response.data; // The response data is assigned to the result variable.
        if (result.success) {
            return result.data // If the status of the response data is "OK", the setReportsCategories function is called with the data from the response.
        } else {
            throw new Error("No se pudo obtener los reportes pendientes, intenta nuevamente más tarde. 🙁"); // If the status is not "OK", an error is thrown with the specified message.
        }
    } catch (error) {
        throw new Error(error); // The error is thrown again
    }
}

export async function declinateReport({ commit }, report) {
    try {
        const response = await privateReportApi.post(`/declinate_report/${report}`);
        if (response.status !== 200) {
            throw new Error(response.statusText); // If the response status is not 200 (OK
        }
        return true;
    } catch (error) {
        throw new Error(error); // The error is thrown again
    }
}

export async function activateReport({ commit }, report) {
    try {
        const response = await privateReportApi.post(`/activate_report/${report}`);
        if (response.status !== 200) {
            throw new Error(response.statusText); // If the response status is not 200 (OK
        }
        return true;
    } catch (error) {
        throw new Error(error); // The error is thrown again
    }
}