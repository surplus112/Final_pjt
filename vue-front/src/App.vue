<template>
  <div id="app">
    <div>
      <router-link to="/">Home</router-link> |
      <router-link to="/accounts/login">login</router-link>
    </div>
    <router-view
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
  methods: {
    setCookie(token) {
      this.$cookies.set('auth-token', token)
      this.isLoggedIn = true
    },
    signup(signupData) {
      axios.post(SERVER_URL + '/rest-auth/signup', signupData)
        .then(res => {
          this.setCookie(res.datd.key)
          this.$router.push({ name: 'Home' })
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