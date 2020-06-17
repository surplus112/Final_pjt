<template>
  <div>
    <h1>Mypage</h1>
    <h3>{{ userInfo }}</h3>
    <div v-for="review in reviews" :key="`review_${review.id}`">
      {{ review.movie.title }}
      {{ review.score }}
      {{ review.content }}
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