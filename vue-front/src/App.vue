<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg">
      <router-link class="text-white" to="/">Home</router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <div class="nav-item">
            <div class="navbar-nav-item">
              <router-link class="text-white" :to="{ name: 'ArticleList' }">ArticleList</router-link> |
            </div>
            <div class="navbar-nav-item">
            <router-link class="text-white" :to="{ name: 'MovieList' }">MovieList</router-link> |
            </div>
            <div class="navbar-nav-item">
            <router-link class="text-white" v-if="isLoggedIn" :to="{ name: 'ArticleCreate' }">New Article</router-link> |
            </div>
          </div>
          <div class="nav-item">
            <div class="navbar-nav-item">
            <router-link class="text-white" v-if="!isLoggedIn" :to="{ name: 'Login' }">Login</router-link> |
            </div>
            <div class="navbar-nav-item">
            <router-link class="text-white" v-if="!isLoggedIn" :to="{ name: 'Signup' }">Signup</router-link> |
            </div>
            <div class="navbar-nav-item">
            <router-link class="text-white " v-if="isLoggedIn" :to="{ name: 'Mypage' }">Mypage</router-link> |
            </div>
            <div class="navbar-nav-item">
            <router-link class="text-white" v-if="isLoggedIn" :to="{ name: 'Logout' }">Logout</router-link> |
            </div>
          </div>
        </div>
      </div>
    </nav>
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
  background-color: #2c3e50;
  width: 100%;
  height: 100%;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: white;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

</style>
