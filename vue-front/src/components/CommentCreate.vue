<template>
  <div>
    <form>
      <div>
        <label for="content">내용</label>
        <span v-if="commentValue">
          <input @keypress.enter.prevent="changeInput" id="content" :value="commentValue" @input="newValue=$event.target.value">
          <button @click.prevent="changeInput" type="submit">수정</button>
        </span>
        <span v-else>
          <input @keypress.enter.prevent="onInput" id="content" v-model="newValue">
          <button @click.prevent="onInput" type="submit">제출</button>
        </span>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'CommentCreate',
  data() {
    return {
      newValue: ''
    }
  },
  props: {
    commentValue: {
      type: String
    }
  },
  methods: {
    onInput() {
      // console.log(e.target.value)
      // console.log(this.newValue)
      this.$emit('submit-comment', this.newValue)
      this.newValue = null
    },
    changeInput() {
      this.$emit('change-comment', this.newValue)
    }
  },
}
</script>

<style>

</style>