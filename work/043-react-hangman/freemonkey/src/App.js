import React, {Component} from 'react';
import {getRandomMovie} from "./data"
import './App.css';
import './index.css';

const GAME_NAME = "Free Monkey";
const HEADER_MSG = "Guess the movie title!";

class App extends Component {

  // TODO: Reset game method, render state variables
  // TODO: Create keyboard with letter buttons
  // TODO: Match chars and update state 
  // TODO: Style buttons based on guess (green if in word, else red) 
  // TODO: Win/loss helpers to check state. 

  constructor(props) {
    super(props);
    this.state = {
    }
  }

  componentDidMount() {
    console.log("Component did mount: ");
    console.log(this);
    this.resetGame();
  }

  resetGame = () => {
    const movie = getRandomMovie();
    console.log(movie);
    this.setState({
      header: HEADER_MSG,
      movie: movie.split(""),
      mask: movie.replace(/[A-Za-z]/g, "_"),
    });
  }

  render() {
    return (
      <div className="App">
        <div id="game">
          <header>
            <h1>{GAME_NAME}</h1>
            <h3>{this.state.header}</h3>
          </header>
          <div> 
            <img src={this.state.image} alt="Game status" />
          </div>
          <div id="mask">
            {this.state.mask}
          </div>
          <div>
            {/* Letter buttons */}
          </div>
        </div>
      </div>
    );
  }
}

export default App;
