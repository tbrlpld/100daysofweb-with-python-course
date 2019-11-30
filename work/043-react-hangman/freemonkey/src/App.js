import React, {Component} from 'react';
import {getRandomMovie} from "./data"
import './App.css';
import './index.css';

const GAME_NAME = "Free Monkey";
const HEADER_MSG = "Guess the movie title!";
const MONKEY_IMG = (num) => `http://projects.bobbelderbos.com/hangman/monkey${num}.png`;
const WIN_IMAGE_POSTFIX = "_wins";
const ALPHABET = "abcdefghijklmnopqrstuvwxyz".split("")
const REPLACE_CHAR = "_"

class App extends Component {

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
      mask: movie.replace(/[A-Za-z]/g, REPLACE_CHAR),
      badGuesses: 0,
    });
  }

  createButtons = () => {
    let buttons = [];
    for (let i = 0; i < ALPHABET.length; i++) {
      const btn = <button className="letter" key={i} onClick={this.charClick}>{ ALPHABET[i].toUpperCase() }</button>;
      buttons.push(btn);
    }
    return buttons;
  }

  charClick = (event) => {
    const clickedButton = event.target;
    console.log(clickedButton.innerHTML);
    let newMask = [];
    let matched = false;
    for (let i = 0; i < this.state.mask.length; i++) {
      if (this.state.mask[i] === REPLACE_CHAR 
        && clickedButton.innerHTML.toLowerCase() === this.state.movie[i].toLowerCase()) {
        newMask.push(this.state.movie[i]);
        matched = true;
      } else {
        newMask.push(this.state.mask[i]);
      }
    }
    console.log("Match: " + matched);
    this.setState({
      mask: newMask,
      badGuesses: matched ? this.state.badGuesses : this.state.badGuesses + 1,
    })
    clickedButton.disabled = true;
    clickedButton.style.backgroundColor = matched ? "green" : "red";
    clickedButton.style.color = "white";
  }

  // TODO: Win/loss helpers to check state. 

  render() {
    return (
      <div className="App">
        <div id="game">
          <header>
            <h1>{GAME_NAME}</h1>
            <h3>{this.state.header}</h3>
          </header>
          <div> 
            <img src={MONKEY_IMG(this.state.badGuesses)} alt="game status" />
          </div>
          <div id="mask">
            {this.state.mask}
          </div>
          <div>
            { this.createButtons() }
          </div>
        </div>
      </div>
    );
  }
}

export default App;
