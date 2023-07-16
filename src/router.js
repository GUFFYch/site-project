import Vue from 'vue';
import VueRouter from 'vue-router';
import HomePage from './views/HomePage.vue';
import AdminPage from './views/AdminPage.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage,
  },
  {
    path: '/admin',
    name: 'admin',
    component: AdminPage,
  },
];

const router = new VueRouter({
  base: process.env.NODE_ENV === 'production' ? '/site-project/' : '/',
  mode: 'history', // Set the mode to 'history'
  routes,
});

export default router;
