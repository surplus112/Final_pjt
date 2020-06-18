<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <router-link class="navbar-brand" to="/">Home</router-link>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <router-link class="text-decoration-none mx-3" :to="{ name: 'ArticleList' }">ArticleList <span class="sr-only">(crrent)</span></router-link>
          </li>
          <!-- <li class="nav-item">
            <router-link class="text-decoration-none mx-3" :to="{ name: 'MovieList' }">MovieList</router-link>
          </li> -->
          <span v-if="isLoggedIn" class="d-flex">
            <li class="nav-item">
              <router-link class="text-decoration-none mx-3" v-if="isLoggedIn" :to="{ name: 'ArticleCreate' }">New Article</router-link>
            </li>
            <li class="nav-item">
              <router-link class="text-decoration-none mx-3" v-if="isLoggedIn" :to="{ name: 'Mypage', params: {name: `${userInfo}` } }">Mypage</router-link>
            </li>
            <li class="nav-item">
              <router-link class="text-decoration-none mx-3" v-if="isLoggedIn" :to="{ name: 'Logout' }">Logout</router-link>
            </li>
          </span>
          <span v-else class="d-flex">
            <li class="nav-item">
              <router-link class="text-decoration-none mx-3" v-if="!isLoggedIn" :to="{ name: 'Login' }">Login</router-link>
            </li>
            <li class="nav-item">
              <router-link class="text-decoration-none mx-3" v-if="!isLoggedIn" :to="{ name: 'Signup' }">Signup</router-link>
            </li>
          </span>
           <!-- <li class="nav-item">
            <router-link class="text-decoration-none mx-3" v-if="isLoggedIn" :to="{ name: 'Mypage', params: {name: `${userInfo}` } }">Mypage</router-link>
          </li>
           <li class="nav-item">
            <router-link class="text-decoration-none mx-3" v-if="isLoggedIn" :to="{ name: 'Logout' }">Logout</router-link>
          </li> -->
        </ul>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
import { mapGetters, mapState } from 'vuex'

export default {
  name: "Navar",
  computed: {
    ...mapGetters(['isLoggedIn']),
    ...mapState(['userInfo'])
  },
}
</script>

<style>

</style>