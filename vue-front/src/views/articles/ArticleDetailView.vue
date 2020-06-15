<template>
  <div>
      <h1>ArticleDetail</h1>
      <div v-if="this.article">
        <p>{{ article.user.username }}</p>
        <p>{{ article.title }}</p>
        <p>{{ article.content }}</p>
        <router-link @click="getArticle(article)" :to="{ name: 'ArticleUpdate', params: { id: article.id } }">
          수정하기
        </router-link>
        <router-link @click.native="deleteArticle" to="/articles/comments/delete">
          삭제하기
        </router-link>
        <router-view :article="this.article" />
        <Comment :article_id="article.id" />
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
      article: null
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