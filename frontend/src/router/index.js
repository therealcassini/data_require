import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/users',
    name: 'Users',
    component: () => import('../views/Users.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/requirements',
    name: 'Requirements',
    component: () => import('../views/Requirements.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/api-test',
    name: 'ApiTest',
    component: () => import('../views/ApiTest.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../views/NotFound.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 路由守卫实现权限拦截
router.beforeEach((to, from, next) => {
  // 检查是否需要登录
  if (to.meta.requiresAuth) {
    // 检查localStorage中是否有登录状态
    const isLoggedIn = localStorage.getItem('token') === 'logged_in';
    
    if (isLoggedIn) {
      next();
    } else {
      // 未登录，跳转到登录页面
      next({ name: 'Login' });
    }
  } else {
    // 不需要登录的页面直接放行
    next();
  }
});

export default router