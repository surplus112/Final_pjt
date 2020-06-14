<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <div>
        <label for="username">ID</label>
        <input v-model="loginData.username" class="form-control" id="username">
      </div>
      <div>
        <label for="password">password</label>
        <input v-model="loginData.password" type="password" class="form=control" id="password">
      </div>
      <button type="submit">확인</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: "LoginView",
  data () {
    return {
      loginData: {
        username: null,
        password: null,
      }
    }
  },
  props: {
    isLoggedIn: {
      type: Boolean
    }
  },
  methods: {
    setCookie(token) {
      this.$cookies.set('auth-token', token)
    },
    login() {
      axios.post(`${SERVER_URL}/rest-auth/login/`, this.loginData)
        .then(res => {
          this.setCookie(res.data.key)
          this.$router.push({ name: 'Home'})
        })
        .catch(err => console.log(err.response.data))
      this.$emit('is-login', this.isLoggedIn)
    },
    // login() {
    //   this.$emit('submit-login-data', this.loginData)
    // }
  }
}
</script>

<style>

</style>