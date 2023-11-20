/**
 * Sets the list of reports in the store.
 * 
 * @param {object} state - The state object.
 * @param {array} reports - The list of reports.
 */
export function setReports(state, reports) {
    reports.forEach(report => {
        state.reports.reports.push(report);
    });
}

/**
 * Clears the list of reports in the store.
 * 
 * @param {object} state - The state object.
 */
export function cleanReports(state) {
    state.reports.reports = [];
}

/**
 * Sets the list of user reports in the store.
 * 
 * @param {object} state - The state object.
 * @param {array} reports - The list of user reports.
 */
export function setUserReports(state, reports) {
    reports.forEach(report => {
        state.reports.userReports.push(report);
    });
}

/**
 * Clears the list of user reports in the store.
 * 
 * @param {object} state - The state object.
 */
export function cleanUserReports(state) {
    state.reports.userReports = [];
}

/**
 * Sets the list of report categories in the store.
 * 
 * @param {object} state - The state object.
 * @param {array} categories - The list of report categories.
 */
export function setReportsCategories(state, categories) {
    // Loop through each category and add it to the store
    categories.forEach(category => {
        state.reports.reportCategories.push(category);
    });
}

/**
 * Clears the list of report categories in the store.
 * 
 * @param {object} state - The state object.
 */
export function cleanReportsCategories(state) {
    // Clear the list of report categories
    state.reports.reportCategories = [];
}