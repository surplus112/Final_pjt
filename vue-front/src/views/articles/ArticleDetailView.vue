<template>
  <div>
      <h1>ArticleDetailView</h1>
      <div v-if="this.article">
        <p>{{ article.user.username }}</p>
        <p>{{ article.title }}</p>
        <p>{{ article.content }}</p>
        <router-link :to="{ name: 'ArticleUpdateView', params: { id: article.id } }">
          수정하기
        </router-link>
        <Comment :article_id="article.id" />
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import Comment from '@/components/Comment.vue'
// import ArticleUpdate from '@/components/ArticleUpdate.vue'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'ArticleDetailView',
  components: {
    Comment,
  },
  data() {
    return {
      article: null
    }
  },
  methods: {
    ArticleUpdate () {
      axios.put(`${SERVER_URL}/articles/${this.article.id}/articleupdate/`)
        .then(res => {
          // console.log(res.data)
          this.articleupdate = res.data
        })
        .catch(err => console.log(err.response.data))
    },
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
    }
  },
  created() {
    this.fetchArtcleDetail()
  }
}
</script>

<style>

</style>