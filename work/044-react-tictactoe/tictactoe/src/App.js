import React, {Component} from 'react';
import './App.css';


const GAME_TITLE = "tic-tac-toe"
const PLAYER_SYMBOLS = ["X", "O"]
const INITIAL_STATE = {
  activePlayer: 1,
  gameStatus: [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
  ],
}

class App extends Component {

  constructor(props) {
    super(props);
    this.state = INITIAL_STATE;
  }

  componentDidMount() {
    console.log("Did mount.")
    // this.resetGame();
  }

  resetGame = () => {
    this.setState(INITIAL_STATE);
    return;
  }

  drawGame = () => {
    const rows = this.state.gameStatus.map(this.drawRow);
    const game = (<div className="game">{ rows }</div>);
    return game;
  }

  drawRow = (row, index) => {
    const rowKey = index;
    console.log("Drawing Row: " + rowKey);
    console.log(row);
    const fields = row.map(this.drawFields);
    return (<div className="field-row" key={index}>{fields}</div>);
  }

  drawFields = (field, index) => {
    const fieldKey = index;
    console.log("Drawing Field: " + fieldKey);
    console.log(field);
    return (<div className="field" key={fieldKey}>{ field }</div>)
  }

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h1>{ GAME_TITLE }</h1>
        </div>
        <div className="game-wrapper">
          {this.drawGame()}
        </div>
      </div>
    );
  }
}

export default App;
