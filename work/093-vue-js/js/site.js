// Write your Vue JavaScript code here.

new Vue({
  el: "#app",
  data: {
    search_text: null,
    movies: dummy_movies.hits,
    genres: dummy_genres,
  },
})