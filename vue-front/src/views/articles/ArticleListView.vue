<template>
  <div>
      <h1>ArticleList</h1>
      <div id="article-list">
        <ul>
          <li v-for="(article, number) in articles" :key="`article_${article.id}`">
            <p>{{ number+1 }}</p>
            <p>{{ article }}</p>
            <router-link :to="{ name: 'ArticleDetail', params: { id: article.id }, query: { number: number} }">{{ article.title }}</router-link>
          </li>
        </ul>
      </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: "ArticleList",
  computed: {
    ...mapState(['articles'])
  },
  methods: {
    ...mapActions(['fetchArticles'])
  },
  created() {
    this.fetchArticles()
  },
}
</script>

<style>

</style>