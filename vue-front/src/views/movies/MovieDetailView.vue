<template>
  <div>
    <div v-if="this.movie">
      <h1>{{ movie.title }}</h1>
      <p>{{ movie.overview }}</p>
    </div>
    <div>
      <router-link :to="{name: 'MovieUpdate', params: {id: movie.id}, query: { number: number} } ">
        수정
      </router-link>
    </div>
    <Review :movieId="movie.id" />
  </div>
</template>

<script>
import axios from 'axios'
import Review from '@/components/Review.vue'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'MovieDetail',
  data () {
    return {
      movie: null,
      number: this.$route.query.number
    }
  },
  components: {
    Review
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