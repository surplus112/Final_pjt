<template>
  <div id="app">
    <div>
      <router-link to="/">Home</router-link> |
      <router-link :to="{ name: 'ArticleList' }">ArticleList</router-link> |
      <router-link :to="{ name: 'MovieList' }">MovieList</router-link> |
      <router-link v-if="isLoggedIn" :to="{ name: 'ArticleCreate' }">New Article</router-link> |
      <router-link v-if="!isLoggedIn" :to="{ name: 'Login' }">Login</router-link> |
      <router-link v-if="!isLoggedIn" :to="{ name: 'Signup' }">Signup</router-link> |
      <router-link v-if="isLoggedIn" :to="{ name: 'Mypage' }">Mypage</router-link> |
      <router-link v-if="isLoggedIn" :to="{ name: 'Logout' }">Logout</router-link> |
    </div>
    <router-view />
  </div>
</template>

<script>

import { mapGetters } from 'vuex'

export default {
  name: 'App',
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  methods: {
  },

}
</script>

<style>
  #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
