<template>
  <div>
    <h1>안녕하세요</h1>
    <div v-if="this.movie">
      <p>{{ movie.title }}</p>
    </div>
  </div>
</template>

<script>

export default {
  name: 'MovieDetail',
  data () {
    return {
      movie: null,
    }
  },
}
</script>

<style>

</style>