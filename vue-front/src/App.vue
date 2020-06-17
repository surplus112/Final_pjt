<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg">
    <router-link class="navbar-brand text-white" to="/">Home</router-link>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <router-link class="text-decoration-none mx-3 text-white" :to="{ name: 'ArticleList' }">자유게시판 <span class="sr-only">(crrent)</span></router-link>
          </li>
          <li class="nav-item">
            <router-link class="text-decoration-none mx-3 text-white" :to="{ name: 'MovieList' }">영화 목록</router-link>
          </li>
          <li class="nav-item">
            <router-link class="text-decoration-none mx-3 text-white" v-if="isLoggedIn" :to="{ name: 'ArticleCreate' }">새 글 작성</router-link>
          </li>
        </ul>
        <ul class="navbar-nav">
           <li class="nav-item">
            <router-link class="text-decoration-none mx-3 text-white" v-if="!isLoggedIn" :to="{ name: 'Login' }">로그인</router-link>
          </li>
           <li class="nav-item">
            <router-link class="text-decoration-none mx-3 text-white" v-if="!isLoggedIn" :to="{ name: 'Signup' }">회원가입</router-link>
          </li>
           <li class="nav-item">
            <router-link class="text-decoration-none mx-3 text-white" v-if="isLoggedIn" :to="{ name: 'Mypage', params: {name: `${userInfo}` } }">My</router-link>
          </li>
           <li class="nav-item">
            <router-link class="text-decoration-none mx-3 text-white" v-if="isLoggedIn" :to="{ name: 'Logout' }">로그아웃</router-link>
          </li>
        </ul>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>

import { mapGetters, mapState } from 'vuex'

export default {
  name: 'App',
  computed: {
    ...mapGetters(['isLoggedIn']),
    ...mapState(['userInfo'])
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
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

</style>
