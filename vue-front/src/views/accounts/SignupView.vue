<template>
  <div>
    <h1>SignupView</h1>
    <form @submit.prevent="signup">
      <div class="form-group">
        <label for="username">ID</label>
        <input v-model="signupData.username" class="form-control" id="username">
      </div>
      <div class="form-group">
        <label for="password">password</label>
        <input v-model="signupData.password1" class="form-control" id="password">
      </div>
      <div class="form-group">
        <label for="password2">Confirm password</label>
        <input v-model="signupData.password2" class="form-control" id="password2">
      </div>
      <button type="submit">확인</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "SignupView",
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
    signup() {
      this.$emit('submit-signup-data', this.signupData)
    }
  }
}
</script>

<style>

</style>