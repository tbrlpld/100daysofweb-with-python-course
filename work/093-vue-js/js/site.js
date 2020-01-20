// Write your Vue JavaScript code here.

new Vue({
  el: "#app",
  data: {
    search_text: null,
    movies: dummy_movies.hits,
    genres: dummy_genres,
  },
  methods: {
    search: function () {
      const text = this.search_text
      console.log("Seached for: " + text)
    },
    top10: function () {
      console.log("Show top 10.")
    },
  },
})