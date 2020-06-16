<template>
  <div>
    <h1>MovieList</h1>
    <div id="movie-list">
      <div v-for="(movie, number) in movies" :key="`movie_${movie.id}`">
        <div>{{ number }}</div>
      <MovieListItem :movie="movie" />
      </div>
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