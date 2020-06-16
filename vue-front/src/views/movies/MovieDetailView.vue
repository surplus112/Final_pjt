<template>
  <div>
    <h1>안녕히계세요 저는 집에 갑니다</h1>
    <div v-if="this.movie">
      <p>{{ movie.title }}</p>
    </div>
    <router-view :movie="this.movie" />
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'MovieDetail',
  data () {
    return {
      movie: Object,
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