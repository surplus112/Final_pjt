<template>
  <div>
    <h1 class="text-white">Signup</h1>
    <form @submit.prevent="signup">
      <div class="form-group">
        <label for="username" class="text-white">ID</label>
        <input v-model="signupData.username" type="text" class="form-control w-50 mx-auto" id="username">
      </div>
      <div class="form-group">
        <label for="password1" class="text-white">Password</label>
        <input v-model="signupData.password1" type="password" class="form-control w-50 mx-auto" id="password1">
      </div>
      <div class="form-group">
        <label for="password2" class="text-white">Confirm Password</label>
        <input v-model="signupData.password2" type="password" class="form-control w-50 mx-auto" id="password2">
      </div>
      <button @click.prevent="signup(signupData)" type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Signup',
  data () {
    return {
      signupData: {
        username: null,
        password1: null,
        password2: null,
      }
    }
  },
  methods: {
    ...mapActions(['signup'])
  }
}
</script>

<style>

</style>