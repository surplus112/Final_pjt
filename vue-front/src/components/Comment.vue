<template>
  <div>
    <h4 class="text-white">----------댓글----------</h4>
    <div v-for="comment in comments" :key="`comment_${comment.id}`">
      <p class="text-white">{{ comment.content }}</p>
      <div v-if="checkComment.isComment && comment.id === checkComment.commentId">
        <CommentCreate :commentValue="checkComment.commentValue" @change-comment="updateComment"/>
      </div>
      <div v-else>
        <button @click="changeIsComment(comment)">수정</button>
        <button @click="deleteComment(comment.id)">삭제</button>
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
      checkComment: {
        isComment: false,
        commentId: null,
        commentValue: null,
      },
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
    changeIsComment(comment) {
      this.checkComment.isComment = !this.checkComment.isComment
      this.checkComment.commentId = comment.id
      this.checkComment.commentValue = comment.content
    },
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
        .then(() => {
          // console.log(res.data)
          this.getCommentList()
        })
        .catch(err => console.log(err.response.data))
    },
    updateComment(content) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }
      this.commentForm.content = content
      axios.put(`${SERVER_URL}/articles/${this.articleId}/comments/${this.checkComment.commentId}/`, this.commentForm, config)
        .then(() => {
          // console.log(res.data)
          this.checkComment.isComment = false
          this.checkComment.commentId = null
          this.checkComment.commentValue = null
          this.getCommentList()
        })
        .catch(err => {
          // console.log(this.commentForm)
          console.log(err)
        })
    },
    deleteComment(deleteCommentId) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }
      axios.delete(`${SERVER_URL}/articles/${this.articleId}/comments/${deleteCommentId}/`, config)
        .then(res => {
          alert(res.data.message)
          this.getCommentList()
        })
        .catch(err => alert(err))
    }
  },
  created() {
    this.getCommentList()
  }
}
</script>

<style>

</style>