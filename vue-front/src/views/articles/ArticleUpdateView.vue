<template>
  <div>
    <h1>ArticleUpdate</h1>
    {{ index }}
    <!-- {{ articles[this.index] }} -->
    <div v-for="article in articles" :key="article.id">
      {{ article.id }}
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import { mapState } from 'vuex'

// const SERVER_URL = 'http://localhost:8000'
// ${this.$route.params.id}

export default {
  name: "ArticleUpdate",
  data() {
    const index = this.$route.params.id
    return {
      index: index,

    }
  },
  computed: {
    ...mapState(['articles'])
  },
  methods: {
    // ArticleUpdate () {
    //   axios.put(`${SERVER_URL}/articles/${this.article.id}/update/`)
    //     .then(res => {
    //       // console.log(res.data)
    //       this.articleupdate = res.data
    //     })
    //     .catch(err => console.log(err.response.data))
    // },
  }
}
</script>

<style>

</style>