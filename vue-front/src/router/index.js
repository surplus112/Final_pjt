import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import LoginView from '@/views/accounts/LoginView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import SignupView from '@/views/accounts/SignupView.vue'
import MypageView from '@/views/accounts/MypageView.vue'

import ArticleListView from '../views/articles/ArticleListView.vue'
import ArticleCreateView from '../views/articles/ArticleCreateView.vue'
import ArticleDetailView from '../views/articles/ArticleDetailView.vue'
import ArticleUpdateView from '../views/articles/ArticleUpdateView.vue'

import MovieListView from '../views/movies/MovieListView.vue'
import MovieDetailView from '../views/movies/MovieDetailView.vue'
import MovieUpdateView from '../views/movies/MovieUpdateView.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/accounts/logout',
    name: 'Logout',
    component: LogoutView
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView
  },
  {
    path: '/accounts/mypage',
    name: 'Mypage',
    component: MypageView
  },
  {
    path: '/articles',
    name: 'ArticleList',
    component: ArticleListView
  },
  {
    path: '/articles/creates',
    name: 'ArticleCreate',
    component: ArticleCreateView
  },
  {
    path: '/articles/:id',
    name: 'ArticleDetail',
    component: ArticleDetailView
  },
  {
    path: '/articles/:id/updates',
    name: 'ArticleUpdate',
    component: ArticleUpdateView
  },
  {
    path: '/movies',
    name: 'MovieList',
    component: MovieListView
  },
  {
    path: '/movies/:id',
    name: 'MovieDetail',
    component: MovieDetailView
  },
  {
    path: '/movies/:id/updates',
    name: 'MovieUpdate',
    component: MovieUpdateView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const publicPages = ['Login', 'Signup', 'Home', 'MovieList', 'MovieDetail']
  const authPages = ['Login', 'Signup']

  const authRequired = !publicPages.includes(to.name)
  const unauthRequired = authPages.includes(to.name)
  const isLoggedIn = !!Vue.$cookies.isKey('auth-token')

  if(unauthRequired && isLoggedIn) {
    next('/')
  }
  authRequired && !isLoggedIn ? next({ name: 'Login' }) : next()
})

export default router
