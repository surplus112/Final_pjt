<template>
  <div>
    <label for="score">평점</label>
    <input id="score" v-model="reviewData.score">
    <label for="content">내용</label>
    <input id="content" v-model="reviewData.content">
    <button @click.prevent="onInput" type="submit">제출</button>
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
    onInput() {
      this.$emit('submit-review', this.reviewData)
      this.reviewData.score = null
      this.reviewData.content = ''
    }
  }
}
</script>

<style>

</style>