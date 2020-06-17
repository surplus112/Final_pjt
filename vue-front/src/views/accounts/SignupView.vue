<template>
  <div class="formContainer" id="loginn">
    <form class="login-box">
      <br>
      <h2>Sign Up</h2>
      <br>
      <br>
      <span>ID    </span><input type="text" v-model="username" name="username" placeholder="ID를 입력하세요" />
      <br>
      <br>
      <span>Password    </span>
      <input type="password" v-model="password1" name="userpassword" placeholder="비밀번호를 입력하세요" />
      <br>
      <br>
      <span>Confirm Password    </span>
      <input type="password" v-model="password2" name="userpassword" placeholder="비밀번호를 입력하세요" />
      <br />
    </form>
    <br />
    <div class="login-btn">
      <input
        type="submit"
        class="btn btn-primary"
        name="submit"
        @click.prevent="signup(signupData)"
        value="회원가입"
      />
    </div>
  </div>
  <!-- <div>
    <h1>Signup</h1>
    <form>
      <div>
        <label for="username">ID</label>
        <input v-model="signupData.username" id="username" type="text">
      </div>
      <div>
        <label for="password1">password</label>
        <input v-model="signupData.password1" id="password1" type="password">
      </div>
      <div>
        <label for="password2">Confirm password</label>
        <input v-model="signupData.password2" id="password2" type="password">
      </div>
      <button @click.prevent="signup(signupData)">확인</button>
    </form>
  </div> -->
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