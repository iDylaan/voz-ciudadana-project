import auth_api from '@/api/auth_api.js';
import router from '@/router';

export async function login({ commit }, payload) {
    try {
        const response = await auth_api.post('/login', {
            email: payload.email,
            password: payload.password
        });

        const { data } = response;
        localStorage.setItem('token', data.accessToken);
        const firstAccess = data.user.first_access == 1 ? true : false;
        commit('setUser', {
            username: data.user.username,
            isAdmin: data.user.is_admin,
            email: data.user.email,
            userID: data.user.id,
            picProfile: data.user.profile_picture,
            bannerProfile: data.user.profile_banner,
            firstAccess: firstAccess
        });
        commit('cleanError');

        if (data.user.is_admin) {
            router.push("/admin");
        } else {
            router.push("/");
        }
    } catch (error) {
        console.log(error);
        if (error.message) {
            commit('setError', error.message);
        } else {
            commit('setError', error.response.data.message);
        }
    }
}
export async function signup({ commit }, payload) {
    try {
        await auth_api.post('/register', {
            email: payload.email,
            password: payload.password,
            username: payload.username
        });
        commit('cleanError');

    } catch (error) {
        commit('setError', error.response.data.message);
        setTimeout(() => {
            commit('cleanError');
        }, 200);
    }
}
export async function logout({ commit }) {
    localStorage.removeItem('token');
    localStorage.removeItem('username');
    localStorage.removeItem('is_admin');
    localStorage.removeItem('email');
    localStorage.removeItem('userID');
    localStorage.removeItem('pic_profile');
    localStorage.removeItem('banner_profile');
    commit('cleanUser');
}