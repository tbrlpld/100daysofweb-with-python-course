// Write your Vue JavaScript code here.


const API_BASE_URL = "http://movie_service.talkpython.fm/api/"
const genre_options = () => ["Select movie genre",].concat(dummy_genres)

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
      // console.log("Seached for: " + text)
      this.load_movies("search/" + text)
    },
    top10: function () {
      // console.log("Show top 10.")
      this.load_movies("movie/top")
    },
    select_genre: function () {
      const genre = this.selected_genre
      console.log("Selected genre: " + genre)
    },
    load_movies: function (endpoint) {
      const app_obj = this
      axios.get(API_BASE_URL + endpoint)
        .then(function (response) {
          // console.log("Success: " + response.data.hits)
          app_obj.movies = response.data.hits
        })
        .catch(function (error) {
          console.log("ERROR: " + error)
        })
    },
  },
})