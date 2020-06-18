import Vue from 'vue'
import Vuex from 'vuex'

import cookies from 'vue-cookies'
import router from '@/router'
import axios from 'axios'

import SERVER from '@/api/drf'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authToken: cookies.get('auth-token'),
    articles: [],
    movies: [],
    userInfo: null,
  },
  getters: {
    isLoggedIn: state => !!state.authToken,
    config: state => ({headers: { Authorization: `Token ${state.authToken}` }})
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.authToken = token
      cookies.set('auth-token', token)
    },
    SET_ARTICLES(state, articles) {
      state.articles = articles
    },
    SET_MOVIES(state, movies) {
      state.movies = movies
    },
    SET_USERINFO(state, userInfo) {
      state.userInfo = userInfo
      window.localStorage.setItem('userInfo', userInfo);
    }
  },
  actions: {
    postAuthData({ commit }, info) {
      axios.post(SERVER.URL + info.location, info.data)
        .then(res => {
          commit('SET_TOKEN', res.data.key)
          router.push({ name: 'Home' })
        })
        .catch(err => alert(err.response))
    },
    signup({ dispatch }, signupData) {
      const info = {
        data: signupData,
        location: SERVER.ROUTES.signup
      }
      dispatch('postAuthData', info)
    },
    login({ dispatch, commit }, loginData) {
      const info = {
        data: loginData,
        location: SERVER.ROUTES.login
      }
      commit('SET_USERINFO', loginData.username)
      dispatch('postAuthData', info)
    },
    logout({ getters, commit }) {
      axios.post(SERVER.URL + SERVER.ROUTES.logout, null, getters.config)
        .then(() => {
          // console.log(res)
          commit('SET_TOKEN', null)
          cookies.remove('auth-token')
          window.localStorage.removeItem('userInfo');
          router.push({ name: 'Home' })
        })
        .catch(err => console.log(err.response.data))
    },
    fetchArticles({ commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.articleList)
        .then(res => commit('SET_ARTICLES', res.data))
        .catch(err => console.log(err))
    },
    fetchMovies({ commit }) {
      axios.get(SERVER.URL + SERVER.ROUTES.movieList)
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.log(err))
    },
  },
  modules: {
  }
})
