
export function setUser(state, payload) {
    state.user.id = payload.userID;
    state.user.email = payload.email;
    state.user.isAdmin = payload.isAdmin;
    state.user.username = payload.username;
    state.user.picProfile = payload.picProfile;
    state.user.bannerProfile = payload.bannerProfile;
    localStorage.setItem('username', payload.username);
    localStorage.setItem('is_admin', payload.isAdmin);
    localStorage.setItem('email', payload.email);
    localStorage.setItem('userID', payload.userID);
    localStorage.setItem('pic_profile', payload.picProfile);
    localStorage.setItem('banner_profile', payload.bannerProfile);
}
export function cleanUser(state) {
    state.user.id = '';
    state.user.email = '';
    state.user.isAdmin = '';
    state.user.username = '';
    state.user.picProfile = '';
    state.user.bannerProfile = ''; 
}
export function setError(state, error) {
    state.error = error;
}
export function cleanError(state) {
    if (state.error !== '') state.error = '';
}