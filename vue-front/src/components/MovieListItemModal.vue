<template>
  <div>
    <h2>movie list item modal</h2>
     <div class="modal fade" :id="movieId" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">{{ movie.title }}</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <img :src="movie.backdropUrl" class="w-100">
          <hr>
          <button class="btn btn-info">{{ movie.user_rating }}</button>
          <p>{{ movie.overview }}</p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div>

  </div>
</template>

<script>
export default {
  name: 'MovieListItemModal',
  props: {
    movie: {
      type: Object,
    },
  },
  computed: {
    movieId() {
      return 'Modal-' + this.movie.id
    },
    backdropUrl() {
      return "https://image.tmdb.org/t/p/w300/" + this.movie.backdrop_path
    },
  },
}
</script>

<style>

</style>