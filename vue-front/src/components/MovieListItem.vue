<template>
  <div class="col-3">
    <div class="card w-100">
      <img :src="posterUrl" class="card-img-top" alt="...">
      <div class="card-body">
        <!-- <div>{{ number+1 }}</div> -->
        <router-link :to="{ name: 'MovieDetail', params: { id: movie.id }, query: { number: number} }">
          <h5 class="card-title">{{ movie.title }}</h5>
        </router-link>
        <p class="card-text"></p>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "MovieListItem",
  data() {
    return {
      number: this.$route.query.number
    }
  },
  props: {
    movie: {
      type: Object,
    }
    // number: {
    //   type: Number
    // },
  },
  computed: {
    posterUrl() {
      return "https://image.tmdb.org/t/p/w300/" + this.movie.poster_path
    },
  },
}
                      
</script>

<style>

</style>