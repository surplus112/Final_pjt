<template>
  <div>
    <span v-if="reviewValue">
      <label for="score">평점</label>
      <input id="score" :value="reviewScore">
      <label for="content">내용</label>
      <input id="content" :value="reviewValue">
      <button @click.prevent="changeInput" type="submit">제출</button>
    </span>
    <span v-else>
      <label for="score">평점</label>
      <input id="score" v-model="reviewData.score">
      <label for="content">내용</label>
      <input id="content" v-model="reviewData.content">
      <button @click.prevent="onInput" type="submit">제출</button>
    </span>
    <!-- <select v-model="status">
      <option value="one">1</option>
      <option value="two">2</option>
      <option value="three">3</option>
      <option value="four">4</option>
      <option value="five">5</option>
    </select> -->
  </div>
</template>

<script>
export default {
  name: 'ReviewCreate',
  props: {
    reviewScore: {
      type: Number
    },
    reviewValue: {
      type: String
    }
  },
  data() {
    return {
      // status: 'one',
      reviewData: {
        score: null,
        content: ''
      }
    }
  },
  methods: {
    // inputValue() {
    //   this.reviewData.score = this.reviewScore
    //   this.reviewData.content = this.reviewValue
    // },
    onInput() {
      this.$emit('submit-review', this.reviewData)
      this.reviewData.score = null
      this.reviewData.content = ''
    },
    changeInput() {
      console.log(this.checkReview)
      this.$emit('change-review', this.reviewData)
    }
  },
}
</script>

<style>

</style>