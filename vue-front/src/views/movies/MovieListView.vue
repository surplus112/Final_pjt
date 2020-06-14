<template>
  <div>
    <h1>MovieList</h1>
    <div id="movie-list">
      <ul>
        <li v-for="movie in movies" :key="`movie_${movie.id}`">
          <p>{{movie.id}}</p>
          <p>{{movie.title}}</p>
          <p>{{movie.release_date}}</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'MovieListView',
  data () {
    return {
      movies: []
    }
  },
  methods : {
    fetchMovies() {
      axios.get(`${SERVER_URL}/movies/`)
        .then(res => {
          this.movies = res.data
        })
        .catch(err => console.log(err.response.data))
    },
  },
  created() {
    this.fetchMovies()
  }
}
</script>

<style>

</style>