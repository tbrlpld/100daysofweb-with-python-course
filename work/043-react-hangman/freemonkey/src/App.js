import React, {Component} from 'react';
import {getRandomMovie} from "./data"
import './App.css';
import './index.css';

const GAME_NAME = "Free Monkey";
const HEADER_MSG = "Guess the movie title!";
const WIN_MSG = "You freed the monkey! :)"
const LOSS_MSG = "Oh no, the monkey is trapped! :("
const MONKEY_IMG = (num) => `http://projects.bobbelderbos.com/hangman/monkey${num}.png`;
const WIN_IMAGE_POSTFIX = "_wins";
const ALPHABET = "abcdefghijklmnopqrstuvwxyz".split("");
const REPLACE_CHAR = "_";
const MAX_GUESSES = 5;

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
    }
  }

  componentDidMount() {
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
      buttonWidget: this.createLetterButtons(),
    });
  }

  createLetterButtons = () => {
    let buttons = [];
    for (let i = 0; i < ALPHABET.length; i++) {
      const btn = <button className="letter" key={i} onClick={this.charClick}>{ ALPHABET[i].toUpperCase() }</button>;
      buttons.push(btn);
    }
    return buttons;
  }

  charClick = (event) => {
    const clickedButton = event.target;
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

    this.setState(
      {
        mask: newMask,
        badGuesses: (matched ? this.state.badGuesses : this.state.badGuesses + 1),
      }, 
      this.checkWinOrLoss  // Callback, after state is updated
    )

    clickedButton.disabled = true;
    clickedButton.style.backgroundColor = matched ? "green" : "red";
    clickedButton.style.color = "white";
  }

  checkWinOrLoss = () => {
    if (this.isWon()) {
      this.onWin();
      return;
    }
    if (this.isLoss()) {
      this.onLoss();
      return;
    }
  }

  // Once all the replacement characters are removed from the mask, the game is won.
  isWon = () => !this.state.mask.includes(REPLACE_CHAR);

  onWin = () => {
    this.setState({
      header: WIN_MSG,
      buttonWidget: this.newGameButton("Play Again"),
      badGuesses: WIN_IMAGE_POSTFIX,  // For win image rendering.
    });
  }

  isLoss = () => this.state.badGuesses >= MAX_GUESSES;

  onLoss = () => {
    this.setState({
      header: LOSS_MSG,
      buttonWidget: this.newGameButton("Try Again"),
    });
  }

  newGameButton = (msg) => {
    return <button onClick={this.resetGame}>{ msg }</button>
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
            <img src={MONKEY_IMG(this.state.badGuesses)} alt="game status" />
          </div>
          <div id="mask">
            {this.state.mask}
          </div>
          <div>
            { this.state.buttonWidget }
          </div>
        </div>
      </div>
    );
  }
}

export default App;
