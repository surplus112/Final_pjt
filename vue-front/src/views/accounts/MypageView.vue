<template>
  <div>
    <h3>{{ userInfo }}님의 Mypage</h3>
    <hr>
    <div v-if="reviews">
      <div v-for="review in reviews" :key="`review_${review.id}`">
        <router-link :to="{ name: 'MovieDetail', params: { id: review.movie.id } }">{{ review.movie.title }}</router-link>
        <p class="mt-3">평점: {{ review.score }}</p>
        <p>리뷰: {{ review.content }}</p>
        <hr>
      </div>
    </div>
    <h2>추천 영화</h2>
    <div id="movie-list" class="row">
      <div class="col-3 padding-0px" v-for="(recommend, number) in myRecommend" :key="`recommend_${recommend.id}`">
        <MovieListItem :movie="recommend" :number="number" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieListItem from '@/components/MovieListItem.vue'

const SERVER_URL = "http://localhost:8000"

export default {
  name: 'Mypage',
  data () {
    return {
      userInfo: window.localStorage.getItem('userInfo'),
      reviews: null,
      myRecommend: []
    }
  },
  components: {
    MovieListItem
  },
  methods: {
    fetchUserReview() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }
      axios.get(`${SERVER_URL}/movies/reviews/${this.userInfo}/`, config)
        .then(res => {
          this.reviews = res.data
        })
        .catch(err => {
          alert(err)
        })
    },
    fetchRecommend() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }
      axios.get(`${SERVER_URL}/movies/recommends/${this.userInfo}/`, config)
        .then(res => {
          this.myRecommend = res.data
        })
        .catch(err => {
          alert(err)
        })
    }
  },
  created() {
    this.fetchRecommend()
  },
  mounted() {
    this.fetchUserReview()
  }
}
</script>

<style>

</style>