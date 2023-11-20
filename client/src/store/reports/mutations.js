export function setReports(state, reports) {
    reports.forEach(report => {
        state.reports.reports.push(report);
    });
}
export function cleanReports(state) {
    state.reports.reports = [];
}
export function setUserReports(state, reports) {
    reports.forEach(report => {
        state.reports.userReports.push(report);
    });
}
export function cleanUserReports(state) {
    state.reports.userReports = [];
}