<template>
  <div>
    <h1>MovieUpdate</h1>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

const SERVER_URL = "http://localhost:8000"


export default {
  name: "MovieUpdate",
  data() {
    const index = this.$router.query.number
    return{
      index: +index,
      movieInfo: {
        title:null,
      }
    }
  },
  props: {
    number: {
      type: Number
    },
  },
  computed: {
    ...mapState(['movies'])
  },
  methods: {
    inputMovieValue() {
      console.log(this.index)
      this.movieInfo.title = this.movies[this.index].title
    },
    movieUpdate() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }
      axios.put(`${SERVER_URL}/movies/${this.$route.params.id}/update/`, this.movieInfo, config)
        .then(() => {
          this.$router.push({ name: 'MovieDetail', params: { id: this.$route.params.id } })
        })
        .catch(err => console.log(err.response.data))
    },
  },
  created() {
    this.inputMovieValue()
  }
}
</script>

<style>

</style>