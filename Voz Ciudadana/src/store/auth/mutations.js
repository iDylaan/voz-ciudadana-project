
export function setUser(state, user) {
    state.user = user;
}
export function cleanUser(state) { state.user = {} }
export function setError(state, error) { state.error = error; }
export function cleanError(state) {
    if (state.error !== '') state.error = '';
}

export function toggleLoading(state) {
    state.isFormLoading = !state.isFormLoading;
}

export function setThemePorfile(state, payload) {
    localStorage.setItem('profile_picture', payload.pic);
    localStorage.setItem('profile_banner', payload.banner);
    localStorage.setItem('first_access', false);
    state.user.profile_picture = payload.pic;
    state.user.profile_banner = payload.banner;
}