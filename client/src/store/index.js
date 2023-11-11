import { createStore } from 'vuex';
import auth from './auth/index.js';

export default createStore({
  modules: {
    auth
  }
})
