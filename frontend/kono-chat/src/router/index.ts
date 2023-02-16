import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Home from '../views/Home.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/kono-chat',
    name: 'kono-chat',
    component: () => import('../views/Kono-Chat.vue'),
  },
  {
    path: '/credits',
    name: 'credits',
    component: () => import('../views/Credits.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
