<template>
  <div id="app">
    <div>
      <router-link to="/">Home</router-link> |
      <router-link :to="{ name: 'MovieListView' }">MovieList</router-link> |
      <router-link v-if="isLoggedIn" :to="{ name: 'ArticleCreateView' }">New Article</router-link> |
      <router-link v-if="isLoggedIn" @click.native="logout" to="{ name: 'LogoutView' }">Logout</router-link> |
      <router-link v-if="isLoggedIn" :to="{ name: 'MypageView' }">Mypage</router-link>
      <router-link v-if="!isLoggedIn" :to="{ name: 'LoginView'}">Login</router-link> |
      <router-link v-if="!isLoggedIn" :to="{ name: 'SignupView'}">Signup</router-link>     
    </div>
    <router-view
      @submit-signup-data="signup"
      @submit-login-data="login"
    />
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'App',
  data () {
    return {
      isLoggedIn: false,
    }
  },
  mounted() {
    this.isLoggedIn = this.$ccokies.iskey('auth-token')
  },
  methods: {
    setCookie(token) {
      this.$cookies.set('auth-token', token)
      this.isLoggedIn = true
    },
    signup(signupData) {
      axios.post(SERVER_URL + '/rest-auth/signup/', signupData)
        .then(res => {
          this.setCookie(res.data.key)
          this.$router.push({ name: 'Home'})
        })
        .catch(err => console.log(err.response.data))
    },
    login(loginData) {
      axios.post(SERVER_URL + '/rest-auth/login/', loginData)
        .then(res => {
          this.setCookie(res.data.key)
          this.$router.push({ name: 'Home'})
        })
        .catch(err => console.log(err.response.data))
    },
    logout() {
      const requestHeaders = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(SERVER_URL + '/rest-auth/logout/', null, requestHeaders)
        .then(() => {
          this.$cookies.remove('auth-token')
          this.isLoggedIn = false
          this.$router.push({ name: 'Home' })
        })
        .catch(err => console.log(err.response.data))
    },
  }
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
