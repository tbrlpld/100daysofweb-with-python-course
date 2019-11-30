import React, {Component} from 'react';
import './App.css';


const GAME_TITLE = "tic-tac-toe"


class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h1>{ GAME_TITLE }</h1>
        </div>
        <div className="game-wrapper">
          <div className="game">
            <div className="field-row">
              <div className="field"></div>
              <div className="field"></div>
              <div className="field"></div>
            </div>
            <div className="field-row">
              <div className="field"></div>
              <div className="field"></div>
              <div className="field"></div>
            </div>
            <div className="field-row">
              <div className="field"></div>
              <div className="field"></div>
              <div className="field"></div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
