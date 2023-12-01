import auth_api from '@/api/auth_api.js';
import { authApi, authApiJWT } from '@/api/authApi.js';
import router from '@/router';
import { jwtDecode } from 'jwt-decode';


export async function login({ commit }, payload) {
    commit('toggleLoading');
    try {
        const response = await fetch('https://voz-ciudadana-auth.fly.dev/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: payload.email,
                password: payload.password
            })
        })
        const result = await response.json();
        if (!response.ok && response.status == 400) {
            throw new Error(result.message);
        }
        const { access_token, nombre, email } = result;
        localStorage.setItem('token', access_token);
        const tokenDecoded = jwtDecode(access_token);
        tokenDecoded.sub.username = tokenDecoded.sub.nombre;
        localStorage.setItem('profile_picture', tokenDecoded.sub.profile_picture);
        localStorage.setItem('profile_banner', tokenDecoded.sub.profile_banner);
        localStorage.setItem('first_access', tokenDecoded.sub.first_access);
        commit('setUser', tokenDecoded.sub);
        commit('cleanError');
        router.push("/");
    } catch (error) {
        throw new Error(error);
    } finally {
        commit('toggleLoading');
    }
}
export async function signup({ commit }, user) {
    commit('toggleLoading');
    try {
        const res = await authApi.post('/auth/register', user)
        if (res.status == 200) {
            const resLog = await authApi.post('/auth/login', user)
            const { access_token, nombre, email } = resLog.data

            const newUser = {
                username: nombre,
                email: email
            }

            localStorage.setItem('token', access_token);
            const tokenDecoded = jwtDecode(access_token);
            tokenDecoded.sub.username = tokenDecoded.sub.nombre;
            localStorage.setItem('profile_picture', tokenDecoded.sub.profile_picture);
            localStorage.setItem('profile_banner', tokenDecoded.sub.profile_banner);
            localStorage.setItem('first_access', tokenDecoded.sub.first_access);
            commit('setUser', newUser);
            router.push({ path: '/' });

            commit('cleanError');
        } else {
            throw new Error('Error al iniciar sesion')
        }

    } catch (error) {
        throw new Error(error);
    } finally {
        commit('toggleLoading');
    }
}
export async function logout({ commit }) {
    localStorage.removeItem('token');
    localStorage.removeItem('profile_picture');
    localStorage.removeItem('profile_banner');
    localStorage.removeItem('first_access');
    commit('cleanUser');
}
export async function updateProfileTheme({ commit }, payload) {
    try {
        const response = await authApiJWT.put('/update_profile_theme/' + payload.user_id, {
            profile_banner: payload.banner,
            profile_picture: payload.pic
        });
        commit('setUser', response.data);
    } catch (error) {
        throw new Error(error);
    }
}