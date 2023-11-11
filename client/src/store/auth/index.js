import * as mutations from './mutations.js';
import * as actions from './actions.js';
import state from './state.js';

export default {
    namespaced: true,
    state,
    mutations,
    actions,
}