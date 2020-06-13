<template>
  <div>
    <h1>MovieList</h1>
    <div id="list">
      <table>
        <thead>
          <tr>
            <th scope="col">id</th>
            <th scope="col">title</th>
            <th scope="col">release_date</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="movie in movies" :key="`movie_${movie.id}`">
            <td>{{movie.id}}</td>
            <td>{{movie.title}}</td>
            <td>{{movie.release_date}}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = "http://localhost:8000"

export default {
  name: "MovieListView",
  data () {
    return {
      movies: []
    }
  },
  methods : {
    fetchMovies() {
      axios.get(SERVER_URL + "/movies/")
        .then(res => this.movies = res.data)
        .catch(err => console.log(err.response.data))
    },
  },
}
</script>

<style>

</style>