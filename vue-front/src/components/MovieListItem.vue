<template>
  <div>
    <h1>MovieListItem</h1>
    <div>
      <img :src="posterUrl" alt="...">
      <div>
        <h5>{{ movie.title }}</h5>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieListItem",
  props: {
    movie: {
      type: Object,
    },
  },
  computed: {
    posterUrl() {
      return "https://image.tmdb.org/t/p/w300/" + this.movie.poster_path
    },
  }
}
</script>

<style>

</style>