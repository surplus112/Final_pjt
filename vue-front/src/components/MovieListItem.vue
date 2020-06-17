<template>
  <div>
    <div id="card" class="card">
      <div id="card-body" class="card-body">
        <!-- <div>{{ number+1 }}</div> -->
        <router-link :to="{ name: 'MovieDetail', params: { id: movie.id }, query: { number: number} }">
          <img :src="posterUrl" class="card-img-top" alt="..."> 
          <!-- <h5 class="card-title">{{ movie.title }}</h5> -->
        </router-link>
        <p class="card-text"></p>
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
    number: {
      type: Number
    },
  },
  computed: {
    posterUrl() {
      return "https://image.tmdb.org/t/p/w400" + this.movie.poster_path
    },
  },
}
                      
</script>

<style>
#card {
  background-color: #2c3e50;
  border: #2c3e50;
}

#card-body {
  background-color: #2c3e50;
}
</style>