<template>
    <div class="login-div" id="loginnn">
    <div class="form-group">
      <label for="username">ID </label>
      <input
        type="text"
        id="username"
        class="form-control"
        placeholder="아이디를 입력해주세요"
        v-model="username"
        style="color:black"
      />
      <div class="form-group">
        <label for="password">Password </label>
        <input
          type="password"
          id="password"
          class="form-control"
          placeholder="비밀번호를 입력해주세요"
          v-model="password"
        />
      </div>
      <button class="btn btn-primary" @click.prevent="login(loginData)">Login</button>
    </div>                
  </div>
  <!-- <div>
    <h1>Login</h1>
    <div>
      <label for="username">ID</label>
      <input v-model="loginData.username" type="text" id="username">
    </div>
    <div>
      <label for="password">password</label>
      <input v-model="loginData.password" type="password" id="password">
    </div>
    <button @click.prevent="login(loginData)">확인</button>
  </div> -->
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