<template>
  <div>
      <h1>ArticleList</h1>
      <div id="article-list">
        <ul>
          <li v-for="article in articles" :key="`article_${article.id}`">
            <p>{{ article }}</p>
            <router-link :to="{ name: 'ArticleDetail', params: { id: article.id } }">{{ article.title }}</router-link>
          </li>
        </ul>
      </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: "ArticleList",
  data () {
    return {
      articles: []
    }
  },
  methods : {
    fetchArticles() {
      axios.get(`${SERVER_URL}/articles/`)
        .then(res => {
          this.articles = res.data
        })
        .catch(err => console.log(err.response.data))
    },
  },
  created() {
    this.fetchArticles()
  }
}
</script>

<style>

</style>