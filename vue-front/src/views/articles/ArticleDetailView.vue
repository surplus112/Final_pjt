<template>
  <div>
      <h1>ArticleDetailView</h1>
      <div>
        {{ article }}
      </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'ArticleDetailView',
  data() {
    return {
      article: null
    }
  },
  methods: {
    fetchArtcleDetail() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }
      axios.post(`${SERVER_URL}/articles/${this.$route.params.id}/`, null, config)
        .then(res => {
          console.log(res.data)
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