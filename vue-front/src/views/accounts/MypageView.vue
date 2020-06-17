<template>
  <div>
    <h3>{{ userInfo }}님의 Mypage</h3>
    <hr>
    <div v-for="review in reviews" :key="`review_${review.id}`">
      <router-link :to="{ name: 'MovieDetail', params: { id: review.movie.id } }">{{ review.movie.title }}</router-link>
      <p class="mt-3">평점: {{ review.score }}</p>
      <p>리뷰: {{ review.content }}</p>
      <hr>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

const SERVER_URL = "http://localhost:8000"

export default {
  name: 'Mypage',
  data () {
    return {
      reviews: null,
    }
  },
  computed: {
    ...mapState(['userInfo'])
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
          console.log(res)
          this.reviews = res.data
        })
        .catch(err => {
          alert(err)
        })
    }
  },
  created() {
    this.fetchUserReview()
  }
}
</script>

<style>

</style>