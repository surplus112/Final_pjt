<template>
  <div v-if="this.movie">
    <div id="movie_detail"> 
      <div class="row">
        <div id="image">
          <img :src="posterUrl" alt="..."> 
        </div>
        <div id="dvTitle">
          <h1>{{ movie.title }}</h1>
        </div>
        <div id="overview">
          <p>{{ movie.overview }}</p>
        </div>
        <router-link :to="{name: 'MovieUpdate', params: {id: movie.id}, query: { number: number} } ">
          수정
        </router-link>
        <router-link @click.native="deleteMovie" to="/movies/review/delete">
          삭제하기
        </router-link>
        <Review :movieId="movie.id" />
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
#img{
  margin:5px;
}

#dvBody {
  width: 800px;
  margin: 10px;
  line-height: 15px;
}

</style>