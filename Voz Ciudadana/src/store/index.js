import { createStore } from 'vuex';
import auth from './auth/index.js';
import users from './users/index.js';
import reports from './reports/index.js';

export default createStore({
  modules: {
    auth,
    users,
    reports
  }
})
