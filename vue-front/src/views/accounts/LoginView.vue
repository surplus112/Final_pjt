<template>
  <div>
      <h1>Login</h1>
      <form @submit.prevent="login">
        <div class="form-group">
          <label for="username">ID</label>
          <input v-model="loginData.username" class="form-control" id="username">
        </div>
        <div class="form-group">
          <label for="password">password</label>
          <input v-model="loginData.password" type="password" class="form=control" id="password">
        </div>
        <button type="submit">확인</button>
      </form>
  </div>
</template>

<script>
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
  methods :{
    login() {
      this.$emit('submit-login-data', this.loginData)
    }
  }
}
</script>

<style>

</style>