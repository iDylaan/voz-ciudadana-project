import { createStore } from 'vuex';
import auth_api from '@/api/auth_api.js';
import jwtDecode from 'jwt-decode';

export default createStore({
  state: {
    "user": {
      "username": null,
      "email": null,
      "isAdmin": false,
      "id": null
    },
    "error": ''
  },
  getters: {
    isAuthenticated() {
      const token = localStorage.getItem('token');
      return !!token;
    }
  },
  mutations: {
    setUser(state, payload) {
      state.user.id = payload.userID;
      state.user.email = payload.email;
      state.user.isAdmin = payload.isAdmin;
      state.user.username = payload.username;
    },
    setError(state, error) {
      state.error = error;
    },
    cleanError(state) {
      if (state.error !== '') state.error = '';
    }
  },
  actions: {
    async login({ commit }, payload) {
      try {
        const response = await auth_api.post('/login', {
          email: payload.email,
          password: payload.password
        });

        const { data } = response;
        localStorage.setItem('token', data.accessToken);
        const tokenDecoded = jwtDecode(localStorage.getItem('token'));
        // console.log(tokenDecoded);
        commit('setUser', {
          username: data.user.username,
          isAdmin: data.user.is_admin,
          email: data.user.email,
          userID: data.user.id,
        });
        commit('cleanError');
      } catch (error) {
        commit('setError', error.response.data.message);
      }
    },
    async signup({ commit }, payload) {
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
    },
    logout({ commit }) {
      localStorage.removeItem('token');
      localStorage.removeItem('username');
      localStorage.removeItem('is_admin');
      localStorage.removeItem('email');
      commit('removeUsername');
      commit('removeEmail');
      commit('removeIsAdmin');
    }
  },
  modules: {
  }
})
