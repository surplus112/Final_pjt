<template>
  <div>
    <div v-if="this.movie">
      <h1>{{ movie.title }}</h1>
      <p>{{ movie.overview }}</p>
    </div>
    <div>
      <router-link :to="{name: 'MovieUpdate', params: {id: movie}} ">수정</router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'MovieDetail',
  data () {
    return {
      movie: null,
    }
  },
  methods: {
    fetchMovieDetail() {
      axios.get(`${SERVER_URL}/movies/${this.$route.params.id}/`)
        .then(res => {
          // console.log(res.data)
          this.movie = res.data
        })
        .catch(err => {console.log(err)})
    },
  },
  created() {
    this.fetchMovieDetail()
  }
}
</script>

<style>

</style>