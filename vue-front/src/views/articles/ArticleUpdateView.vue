<template>
  <div>
    <h1>ArticleUpdate</h1>
    {{ article }}
  </div>
</template>

<script>
// import axios from 'axios'

// const SERVER_URL = 'http://localhost:8000'

export default {
  name: "ArticleUpdateView",
  props: {
    article: {
      type: Object
    }
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