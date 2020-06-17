<template>
  <div>
    <div v-if="this.article">
      <p class="text-white"> ID: {{ article.user.username }}</p>
      <p class="text-white"> 제목: {{ article.title }}</p>
      <p class="text-white"> 내용: {{ article.content }}</p>
      <router-link class="text-white" :to="{ name: 'ArticleUpdate', params: { id: article.id }, query: { number: number} }">
        수정
      </router-link>
      <router-link class="text-white" @click.native="deleteArticle" to="/articles/comments/delete">
        삭제
      </router-link>
      <!-- <router-view :article="this.article" /> -->
      <Comment :articleId="article.id" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import Comment from '@/components/Comment.vue'

// import { mapActions } from 'vuex'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'ArticleDetail',
  components: {
    Comment,
  },
  data() {
    return {
      article: null,
      number: this.$route.query.number
    }
  },
  methods: {
    // ...mapActions(['getArticle']),
    fetchArtcleDetail() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }
      axios.post(`${SERVER_URL}/articles/${this.$route.params.id}/`, null, config)
        .then(res => {
          // console.log(res.data)
          this.article = res.data
        })
        .catch(err => {console.log(err)})
    },
    deleteArticle() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }
      axios.delete(`${SERVER_URL}/articles/${this.article.id}/update/`, config)
        .then(res => {
          // console.log(res.data.message)
          this.$router.push({ name: 'ArticleList' })
          alert(res.data.message)
        })
        .catch(err => alert(err))
    }
  },
  created() {
    this.fetchArtcleDetail()
  }
}
</script>

<style>

</style>

