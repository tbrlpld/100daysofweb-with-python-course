// Write your Vue JavaScript code here.


const API_BASE_URL = "http://movie_service.talkpython.fm/api/"
const SELECT_GENRE_TEXT = "Top movies by genre"

app = new Vue({
  el: "#app",
  data: {
    search_text: null,
    movies: [],
    genres: [SELECT_GENRE_TEXT],
    selected_genre: SELECT_GENRE_TEXT,
  },
  methods: {
    init: function () {
      console.log("initilizing")
      this.load_all_genres()
      this.selected_genre = SELECT_GENRE_TEXT
      this.top10()
    },
    search: function () {
      const text = this.search_text
      this.resetGenre()
      this.load_movies("search/" + text)
    },
    top10: function () {
      // console.log("Show top 10.")
      this.clearInput()
      this.resetGenre()
      this.load_movies("movie/top")
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
    load_all_genres: function () {
      const app_obj = this
      axios.get(API_BASE_URL + "movie/genre/all")
        .then(function (response) {
          let genres = response.data
          genres.unshift(SELECT_GENRE_TEXT)
          app_obj.genres = genres
        })
        .catch(function (error) {
          console.log("ERROR: " + error)
        })
    },
    getGenreMovies: function () {
      this.clearInput()
      this.load_movies("movie/genre/" + this.selected_genre)
    },
    clearInput: function () {
      this.search_text = null
    },
    resetGenre: function () {
     this.selected_genre = SELECT_GENRE_TEXT
    },
  },
})

app.init()