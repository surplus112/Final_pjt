<template>
  <div>
    <h1 class="text-white">Login</h1>
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="username" class="text-white">ID</label>
        <input v-model="loginData.username" type="text" class="form-control w-50 mx-auto" id="username">
      </div>
      <div class="form-group">
        <label for="password" class="text-white">Password</label>
        <input v-model="loginData.password" type="password" class="form-control w-50 mx-auto" id="password">
      </div>
      <button @click.prevent="login(loginData)" type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Login',
  data () {
    return {
      loginData: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    ...mapActions(['login'])
  }
}
</script>

<style>

</style>