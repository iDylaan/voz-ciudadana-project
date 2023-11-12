
export function setUser(state, payload) {
    state.user.id = payload.userID;
    state.user.email = payload.email;
    state.user.isAdmin = payload.isAdmin;
    state.user.username = payload.username;
    state.user.picProfile = payload.picProfile;
    state.user.bannerProfile = payload.bannerProfile;
    state.user.firstAccess = payload.firstAccess;
    localStorage.setItem('username', payload.username);
    localStorage.setItem('is_admin', payload.isAdmin);
    localStorage.setItem('email', payload.email);
    localStorage.setItem('userID', payload.userID);
    localStorage.setItem('pic_profile', payload.picProfile);
    localStorage.setItem('banner_profile', payload.bannerProfile);
    localStorage.setItem('first_access', payload.firstAccess);
}
export function cleanUser(state) {
    state.user.id = null;
    state.user.email = null;
    state.user.isAdmin = false;
    state.user.username = null;
    state.user.picProfile = null;
    state.user.bannerProfile = null; 
    state.user.firstAccess = null;
}
export function setError(state, error) {
    state.error = error;
}
export function cleanError(state) {
    if (state.error !== '') state.error = '';
}