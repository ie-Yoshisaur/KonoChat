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
    path: '/credit',
    name: 'credit',
    component: () => import('../views/Credit.vue'),
  },
];

const router = createRouter({
  history: createWebHistory('/~e205723/kono-chat/'),
  routes,
});

export default router;
