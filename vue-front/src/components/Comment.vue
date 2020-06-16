<template>
  <div>
    <h1>댓글</h1>
    <div v-for="comment in comments" :key="`comment_${comment.id}`">
      {{ comment }}
      <div>
        <button>수정</button>
        <button>삭제</button>
      </div>
    </div>
    <!-- 댓글 폼 만들고, 버튼 누르면 메서드 실행 -->
    <CommentCreate @submit-comment="createComment" />
    <!-- <form @submit.prevent="createComment">
      <div>
        <label for="content">내용</label>
        <input v-model="commentForm.content" id="content">
      </div>
      <button type="submit">제출</button>
    </form> -->
  </div>
</template>

<script>
import CommentCreate from './CommentCreate.vue'
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'Comment',
  components: {
    CommentCreate
  },
  data() {
    return {
      comments: null,
      commentForm: {
        content: null
      }
    }
  },
  props: {
    articleId: {
      type: Number
    }
  },
  methods: {
    // 댓글을 아예 db에 넣어서해보기!!!
    getCommentList() {
      axios.get(`${SERVER_URL}/articles/${this.articleId}/comments/`)
        .then(res => {
          // console.log(res.data)
          this.comments = res.data
        })
        .catch(err => console.log(err.response.data))
    },
    createComment(content) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }
      this.commentForm.content = content
      axios.post(`${SERVER_URL}/articles/${this.articleId}/comments/create/`, this.commentForm, config)
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