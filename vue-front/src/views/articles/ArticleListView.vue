<template>
  <div>
    <h1 class="text-white">자유게시판</h1>
      <div id="article-list">
        <table class="table article-table mt-3">
          <thead>
            <tr>
              <th scope="col" class="text-white">#</th>
              <th scope="col" class="text-white">제목</th>
              <th scope="col" class="text-white">작성자</th>
            </tr>
          </thead>
          <tbody>
            <tr class="text-white" v-for="article in articles" :key="`article_${article.id}`">
              <td>{{article.id}}</td>
              <td><router-link class="text-decoration-none text-white" :to="{ name: 'ArticleDetail', params: { id: article.id }, query: { number: number} }">{{ article.title }}</router-link></td>
              <td>{{ article.user.username }}</td>
            </tr>
          </tbody>
        </table>
      </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: "ArticleList",
  // data() {
  //   return {
  //     article: null
  //   }
  // },
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