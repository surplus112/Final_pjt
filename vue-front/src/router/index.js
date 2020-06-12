import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import LoginView from '../views/accounts/LoginView.vue'
import LogoutView from '../views/accounts/LogoutView.vue'
import SignupView from '../views/accounts/SignupView.vue'
import UserUpdateView from '../views/accounts/UserUpdateView.vue'


Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/accounts/logout',
    name: 'LogoutView',
    component: LogoutView
  },
  {
    path: '/accounts/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/accounts/userupdate',
    name: 'UserUpdateView',
    component: UserUpdateView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
