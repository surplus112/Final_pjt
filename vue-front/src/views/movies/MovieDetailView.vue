<template>
  <div>
    <div v-if="this.movie">
      <h1>{{ movie.title }}</h1>
      <p>{{ movie.overview }}</p>
      <router-link :to="{name: 'MovieUpdate', params: {id: movie.id}, query: { number: number} } ">
        수정
      </router-link>
      <router-link @click.native="deleteMovie" to="/movies/review/delete">
        삭제하기
      </router-link>
      <Review :movieId="movie.id" />
    </div>
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
    deleteMovie() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }
      axios.delete(`${SERVER_URL}/movies/${this.movie.id}/update/`, config)
        .then(res => {
          // console.log(res.data.message)
          this.$router.push({ name: 'MovieList' })
          alert(res.data.message)
        })
        .catch(err => alert(err))
    }
  },
  created() {
    this.fetchMovieDetail()
  }
}
</script>
<style>

</style>