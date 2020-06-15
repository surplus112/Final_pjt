<!--- <template>
  <div>
    <h1>MovieListItem</h1>
    <div>
        <h5>-------------{{ movie.title }}-------------</h5>
      <div>
        <img :src="posterUrl" alt="...">
      </div>
      <div>
        <a href="#" class="btn btn-outline-primary" data-toggle="modal" :data-target="movieId">영화 정보 상세보기</a>
      </div>
    </div>
    <MovieListItemModal :movie="movie" />
  </div>
</template> -->
<template>
  <div class="col-3">
    <div class="card w-100">
      <img :src="posterUrl" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <p class="card-text"></p>
        <a href="#" class="btn btn-outline-primary" data-toggle="modal" :data-target="movieId">영화 정보 상세보기</a>
      </div>
    </div>
    <MovieListItemModal :movie="movie" />
  </div>

</template>

<script>
import MovieListItemModal from '@/components/MovieListItemModal.vue'

export default {
  name: "MovieListItem",
  props: {
    movie: {
      type: Object,
    },
  },
  components:{
    MovieListItemModal,
  },
  computed: {
    posterUrl() {
      return "https://image.tmdb.org/t/p/w300/" + this.movie.poster_path
    },
    movieId() {
      return '#Modal-' + this.movie.id
    },
  },
}
                      
</script>

<style>

</style>