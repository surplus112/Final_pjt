<template>
  <div>
    <h1 class="text-white">새 글 작성</h1>
    <form @submit.prevent="createArticle">
      <div class="form-group">
        <label for="title" class="text-white">Title</label>
        <input v-model="articleData.title" type="text" class="form-control w-50 mx-auto" id="title">
      </div>
      <div class="form-group">
        <label for="content" class="text-white">Content</label>
        <textarea v-model="articleData.content" class="form-control w-50 mx-auto" id="content" rows="3"></textarea>
      </div>
      <div>
        <button @click.prevent="createArticle">Submit!</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = "http://localhost:8000"

export default {
  name: "ArticleCreate",
  data () {
    return {
      articleData: {
        title: null,
        content: null,
      }
    }
  },
  methods : {
    createArticle() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }
      axios.post(SERVER_URL + '/articles/create/', this.articleData, config)
        .then(() => {
          // console.log(res.data)
          this.$router.push({ name: 'ArticleList' })
        })
        .catch(err => console.log(err.response.data))
    }
  }
}
</script>

<style>

</style>