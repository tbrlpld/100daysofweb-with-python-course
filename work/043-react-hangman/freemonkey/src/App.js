import React, {Component} from 'react';
import './App.css';
import './index.css';

const GAME_NAME = "Free Monkey";


class App extends Component {

  // TODO: Define `constructor` and `componentDidMount`
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
    this.setState({
      header: GAME_NAME,
    })
  }

  render() {
    return (
      <div className="App">
        <div id="game">
          <header>
            <h1>{this.state.header}</h1>
          </header>
          <div> 
            <img src={this.state.image} alt="Game status image" />
          </div>
          <div id="mask">
            The Guess Word
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
