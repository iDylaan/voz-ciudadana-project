import { createRouter, createWebHistory } from 'vue-router';
import { useStore } from 'vuex';
import { tokenExpired } from '@/utils/misc.js';
import { jwtDecode } from 'jwt-decode';

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
    path: '/reports',
    name: 'reports',
    component: () => import('../views/Reports.vue')
  },
  {
    path: '/quienes-somos',
    name: 'quienes-somos',
    component: () => import('../views/QuienesSomos.vue')
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
    "path": "/new-report",
    "name": "new-report",
    "component": () => import("../views/NewReport.vue"),
    "meta": { requiresAuth: true },
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
    const tokenDecoded = jwtDecode(token);
    tokenDecoded.sub.username = tokenDecoded.sub.nombre;
    const bannerLS = localStorage.getItem('profile_banner');
    const picLS = localStorage.getItem('profile_picture');
    tokenDecoded.sub.profile_banner = bannerLS ? bannerLS : tokenDecoded.sub.profile_banner;
    tokenDecoded.sub.profile_picture = picLS ? picLS : tokenDecoded.sub.profile_picture;
    store.commit('auth/setUser', tokenDecoded.sub);
    // Verificación de roles.
    if (to.meta.adminRoutes && !is_admin) {
      next({ path: '/not-allowed', hash: '' });
      return;
    }
  }

  next();
});

export default router;