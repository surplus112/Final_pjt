<template>
  <div>
    <h1>댓글</h1>
    <!-- 문제점. user의 id값만 나오고 username이 안보임 -->
    {{ article_id }}
    <div v-for="comment in comments" :key="`comment_${comment.id}`">
      {{ comment }}
    </div>
    <!-- 댓글 폼 만들고, 버튼 누르면 메서드 실행 -->
    <form @submit.prevent="createComment">
      <div>
        <label for="content">내용</label>
        <input v-model="commentForm.content" id="content">
      </div>
      <button type="submit">제출</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'Comment',
  data() {
    return {
      comments: null,
      commentForm: {
        content: null,
        article: this.article_id
      }
    }
  },
  props: {
    article_id: {
      type: Number
    }
  },
  methods: {
    // 댓글을 아예 db에 넣어서해보기!!!
    getCommentList() {
      axios.get(`${SERVER_URL}/articles/${this.article_id}/comments/`)
        .then(res => {
          // console.log(res.data)
          this.comments = res.data
        })
        .catch(err => console.log(err.response.data))
    },
    createComment() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }
      axios.post(`${SERVER_URL}/articles/${this.article_id}/comments/create/`, this.commentForm, config)
        .then(res => {
          console.log(res.data)
          this.getCommentList()
        })
        .catch(err => console.log(err.response.data))
    }
  },
  created() {
    this.getCommentList()
  }
}
</script>

<style>

</style>