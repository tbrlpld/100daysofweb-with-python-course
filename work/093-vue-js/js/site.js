// Write your Vue JavaScript code here.

genre_options = () => ["Select movie genre"].concat(dummy_genres)

new Vue({
  el: "#app",
  data: {
    search_text: null,
    movies: dummy_movies.hits,
    genres: genre_options(),
    selected_genre: genre_options()[0],
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