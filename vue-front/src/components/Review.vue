<template>
  <div id="review">
    <h1>리뷰</h1>
    <div v-for="review in reviews" :key="`review_${review.id}`">
      {{ review }}
      <div v-if="checkReview.isReview && review.id === checkReview.reviewId">
        <ReviewCreate :reviewScore="checkReview.reviewScore" :reviewValue="checkReview.reviewValue" @change-review="updateReview" />
      </div>
      <div v-else>
        <button @click="changeIsReview(review)">수정</button>
        <button @click="deleteReview(review.id)">삭제</button>
      </div>
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
        reviewScore: null,
        reviewValue: null,
      },
      reviewForm: {
        score: null,
        content: null,
      }
    }
  },
  methods: {
    changeIsReview(review) {
      this.checkReview.isReview = !this.checkReview.isReview
      this.checkReview.reviewId = review.id
      this.checkReview.reviewScore = review.score
      this.checkReview.reviewValue = review.content
    },
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
    },
    updateReview(review) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }
      axios.put(`${SERVER_URL}/movies/${this.movieId}/reviews/${this.checkReview.reviewId}/`, review, config)
        .then(() => {
          // console.log(res.data)
          this.checkReview.isReview = false
          this.checkReview.reviewId = null
          this.checkReview.reviewScore = null
          this.checkReview.reviewValue = null
          this.getReviewList()
        })
        .catch(err => {
          // console.log(this.commentForm)
          console.log(err)
        })
    },
    deleteReview(deleteReviewId) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }
      axios.delete(`${SERVER_URL}/movies/${this.movieId}/reviews/${deleteReviewId}/`, config)
        .then(res => {
          alert(res.data.message)
          this.getReviewList()
        })
        .catch(err => alert(err))
    }
  },
  created() {
    this.getReviewList()
  }
}
</script>

<style>

</style>