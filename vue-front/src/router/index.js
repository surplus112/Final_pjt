import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import LoginView from '../views/accounts/LoginView.vue'
import LogoutView from '../views/accounts/LogoutView.vue'
import SignupView from '../views/accounts/SignupView.vue'
import MypageView from '../views/accounts/MypageView.vue'

import ArticleListView from '../views/articles/ArticleListView.vue'
import ArticleCreateView from '../views/articles/ArticleCreateView.vue'
import ArticleDetailView from '../views/articles/ArticleDetailView.vue'
import ArticleUpdateView from '../views/articles/ArticleUpdateView.vue'

import MovieListView from '../views/movies/MovieListView.vue'

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
    path: '/accounts/mypage',
    name: 'MypageView',
    component: MypageView
  },
  {
    path: '/articles',
    name: 'ArticleListView',
    component: ArticleListView
  },
  {
    path: '/articles/articlecreate',
    name: 'ArticleCreateView',
    component: ArticleCreateView
  },
  {
    path: '/articles/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView
  },
  {
    path: '/articles/:id/articleupdate',
    name: 'ArticleUpdateView',
    component: ArticleUpdateView
  },
  {
    path: '/movies/movielist',
    name: 'MovieListView',
    component: MovieListView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
