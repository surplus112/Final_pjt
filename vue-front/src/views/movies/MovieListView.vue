<template>
  <div>
    <h1>MovieList</h1>
    <div id="movie-list">
      <ul>
        <li v-for="movie in movies" :key="`movie_${movie.id}`">
          <p>{{movie.id}}</p>
          <p>{{movie.title}}</p>
          <p>{{movie.release_date}}</p>
          <MovieListItem :movie="movie" />
        </li>
      </ul>
    </div>
  </div>
</template> 

<script>
import { mapState, mapActions } from 'vuex'
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  name: 'MovieList',
  computed: {
    ...mapState(['movies'])
  },
  methods: {
    ...mapActions(['fetchMovies'])
  },
  created() {
    this.fetchMovies()
  },
  components : {
    MovieListItem,
  }, 

  
}
</script>

<style>

</style>