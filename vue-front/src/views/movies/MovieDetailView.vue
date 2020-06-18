<template>
  <div class="container">
    <div id="movie_detail" class="row"> 
          <div id="dvTitle" class="text-white">
            <h1 class="text-white">{{ movie.title }}</h1>
          </div>
      <div class="col-12 row">
        <div class="col-6">
          <img :src="posterUrl" class="w-100" alt="..."> 
        </div>
        <div id="overview" class="col-6 text-white">
          <p class="text-white">줄거리</p>
          <p>{{ movie.overview }}</p>
        </div>
        <div class="col-12 text-center">
        <router-link class="text-white" :to="{name: 'MovieUpdate', params: {id: movie.id}, query: { number: number} } ">
          수정
        </router-link>
        <router-link class="text-white" @click.native="deleteMovie" to="/movies/review/delete">
          삭제
        </router-link>
        </div>
        <div class="col-12">
          <Review :movieId="movie.id" />
        </div>
      </div>
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
    Review,
  },
  computed: {
    posterUrl() {
      return "https://image.tmdb.org/t/p/original" + this.movie.poster_path
    },
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
/* #img{
  margin:5px;
}

#dvBody {
  width: 800px;
  margin: 10px;
  line-height: 15px;
} */

</style>