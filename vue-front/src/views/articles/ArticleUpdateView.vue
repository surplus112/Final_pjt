<template>
  <div>
    <h1>ArticleUpdate</h1>
    <div>
      <label for="title">title: </label>
      <input id="tltle" type="text" v-model="articleInfo.title">
    </div>
    <div>
      <label for="content">content: </label>
      <textarea id="content" cols="30" rows="10" v-model="articleInfo.content"></textarea>
    </div>
    <div>
      <button @click.prevent="articleUpdate">Submit</button>
    </div>
  </div>
</template>

<script>
// console.log(this.$route.query)
import axios from 'axios'

import { mapState } from 'vuex'

const SERVER_URL = "http://localhost:8000"

export default {
  name: "ArticleUpdate",
  data() {
    // const index = this.$route.params.id
    const index = this.$route.query.number
    // const index = this.number
    return {
      index: +index,
      // index: this.number,
      articleInfo: {
        title: null,
        content: null,
      }
    }
  },
  props: {
    number: {
      type: Number
    }
  },
  computed: {
    ...mapState(['articles'])
  },
  methods: {
    inputValue() {
      // this.articleInfo.title = this.articles[this.index].title
      console.log(this.index)
      this.articleInfo.title = this.articles[this.index].title
      this.articleInfo.content = this.articles[this.index].content
    },
    articleUpdate() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }
      axios.put(`${SERVER_URL}/articles/${this.$route.params.id}/update/`, this.articleInfo, config)
        .then(() => {
          // console.log(res.data)
          this.$router.push({ name: 'ArticleDetail', params: { id: this.$route.params.id } })
        })
        .catch(err => console.log(err.response.data))
    },
  },
  created() {
    this.inputValue()
  },
}
</script>

<style>

</style>