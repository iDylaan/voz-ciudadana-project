import { createRouter, createWebHistory } from 'vue-router';
import { useStore } from 'vuex';
import { tokenExpired } from '@/utils/misc.js';

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
  {
    path: '/not-allowed',
    name: 'not-allowed',
    component: () => import('../views/NotAllowed.vue')
  },
  {
    path: '/:catchAll(.*)',
    name: 'not-found',
    component: () => import('../views/NotFound.vue')
  },
  {
    path: '/reportes',
    name: 'reportes',
    component: () => import('../views/Reportes.vue')
  },
  
]

const adminRoutes = [
  {
    "path": "/admin",
    "name": "admin-home",
    "component": () => import("../views/AdminHome.vue"),
    "meta": { requiresAuth: true, isAdmin: true },
  }
]

const userRoutes = [
  {

  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: [...publicRoutes, ...adminRoutes, ...userRoutes]
})

router.beforeEach(async (to, from, next) => {
  const store = useStore();
  const token = localStorage.getItem('token');
  const isAuthenticated = token && !tokenExpired(token);
  const isAdmin = localStorage.getItem('is_admin');

  if (to.path === '/login' || to.path === '/signup') {
    if (isAuthenticated) {
      // Si el usuario ya está autenticado y está tratando de acceder a la página de autenticación, redirige a la página principal.
      next({ path: '/', hash: '' });
      return;
    }
  }

  if (!isAuthenticated && to.meta.requiresAuth) {
    // Si el usuario no está autenticado y está tratando de acceder a una ruta protegida, redirige a la página de autenticación.
    store.getters.logout;
    next({ path: '/login', hash: '' });
    return;
  }

  if (isAuthenticated) {
    // Verificación de roles.
    if (to.meta.adminRoutes && isAdmin) {
      next({ path: '/not-allowed', hash: '' });
      return;
    }
    if (to.meta.userRoutes && !isAdmin) {
      next({ path: '/not-allowed', hash: '' });
      return;
    }
  }

  next();
});

export default router
