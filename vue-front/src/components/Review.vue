<template>
  <div>
    <h1>리뷰</h1>
    <div v-for="review in reviews" :key="`review_${review.id}`">
      {{ review }}
    </div>
    <ReviewCreate @submit-review="createReview" />
  </div>
</template>

<script>
import ReviewCreate from './ReviewCreate.vue'
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'Review',
  components: {
    ReviewCreate
  },
  props: {
    movieId: {
      type: Number
    }
  },
  data() {
    return {
      reviews: null,
      checkReview: {
        isReview: false,
        reviewId: null,
        reviewValue: null,
      },
      reviewForm: {
        score: null,
        content: null,
      }
    }
  },
  methods: {
    getReviewList() {
      axios.get(`${SERVER_URL}/movies/${this.movieId}/reviews/`)
        .then(res => {
          console.log(res.data)
          this.reviews = res.data
        })
        .catch(err => console.log(err.response.data))
    },
    createReview(review) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }
      this.reviewForm.score = review.score
      this.reviewForm.content = review.content
      axios.post(`${SERVER_URL}/movies/${this.movieId}/reviews/create/`, this.reviewForm, config)
        .then(res => {
          console.log(res.data)
          this.getReviewList()
        })
        .catch(err => console.log(err.response.data))
    }
  },
  created() {
    this.getReviewList()
  }
}
</script>

<style>

</style>