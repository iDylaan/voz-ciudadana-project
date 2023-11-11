import { createRouter, createWebHistory } from 'vue-router';
import { useStore } from 'vuex';

const publicRoutes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/HomeView.vue') 
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('../views/Signup.vue')
  },
] 

const adminRoutes = [
  {}  
]

const userRoutes = [
  {
    
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: [...publicRoutes, ...adminRoutes, ...userRoutes]
})

// router.beforeEach(async (to, from, next) => {
//   const store = useStore();
//   const token = store.state.token || localStorage.getItem('token');
//   const isAuthenticated = token && !tokenExpired(token);

//   if (to.path === '/auth' && isAuthenticated) {
//     // Si el usuario ya está autenticado y está tratando de acceder a la página de autenticación, redirige a la página principal.
//     next({ path: '/', hash: '' });
//     return;
//   }

//   if (!isAuthenticated && to.meta.requiresAuth) {
//     // Si el usuario no está autenticado y está tratando de acceder a una ruta protegida, redirige a la página de autenticación.
//     store.dispatch("logout");
//     next({ path: '/auth', hash: '' });
//     return;
//   }

//   if (isAuthenticated) {
//     const decodedToken = jwtDecode(token);
//     const userRoleID = decodedToken.sub.user_role;
//     const userID = decodedToken.sub.user_id;
//     let userRole = '';

//     try {
//       const response = await fetch(`${URL_BASE}/usuarios/test_user_role/${userID}/${userRoleID}`, {
//         method: 'GET',
//         headers: {
//           'Content-Type': 'application/json',
//           'Authorization': `Bearer ${token}`
//         },
//       });

//       if (!response.ok) throw new Error(response.statusText);

//       const data = await response.json();
//       if (data.success) userRole = data.role.name;
//     } catch (err) {
//       store.dispatch('logout');
//       next({ path: '/auth', hash: '' });
//       return;
//     }

//     // Verificación de roles.
//     if (to.meta.adminRoute && userRole !== ROLES.ADMIN) {
//       next({ path: '/not-allowed', hash: '' });
//       return;
//     }

//     if (to.meta.internalRoute && userRole !== ROLES.USER_INT) {
//       next({ path: '/not-allowed', hash: '' });
//       return;
//     }

//     if (to.meta.externalRoute && userRole !== ROLES.USER_INT) {
//       next({ path: '/not-allowed', hash: '' });
//       return;
//     }
//   }

//   next();
// });

export default router
