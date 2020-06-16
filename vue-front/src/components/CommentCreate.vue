<template>
  <div>
    <h1>댓글을 작성해주세요</h1>
    <form>
      <div>
        <label for="content">내용</label>
        <input @keypress.enter.prevent="onInput" id="content">
      </div>
      <button type="submit">제출</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'CommentCreate',
  methods: {
    onInput(e) {
      // console.log(e.target.value)
      this.$emit('submit-comment', e.target.value)
    },
  },
}
</script>

<style>

</style>