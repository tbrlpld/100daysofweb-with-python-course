import React, {Component} from 'react';
import './App.css';


const GAME_TITLE = "tic-tac-toe"
const PLAYER_SYMBOLS = ["X", "O"]
const INITIAL_STATE = {
  activePlayer: 1,
  gameStatus: [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
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

  activePlayerSymbol = () => PLAYER_SYMBOLS[this.state.activePlayer - 1];

  drawPlayerHead = () => {
    let playerOneClasses = ["player"]
    let playerTwoClasses = ["player"]
    if (this.state.activePlayer === 1) {
      playerOneClasses.push("active-player")
    } else if (this.state.activePlayer === 2) {
      playerTwoClasses.push("active-player")
    }
    const playerOneElement = (<div className={playerOneClasses.join(" ")}>Player {PLAYER_SYMBOLS[0]}</div>);
    const playerTwoElement = (<div className={playerTwoClasses.join(" ")}>Player {PLAYER_SYMBOLS[1]}</div>);
    return (<div className="player-header">{playerOneElement}{playerTwoElement}</div>);
  }

  drawGame = () => {
    const rows = this.state.gameStatus.map(this.drawRow);
    const game = (<div className="game">{ rows }</div>);
    return game;
  }

  drawRow = (row, index) => {
    const fields = row.map(this.drawFields);
    return (<div className="field-row" row-index={index} key={index}>{fields}</div>);
  }

  drawFields = (field, index) => {
    return (
      <div className="field" field-index={index} key={index} onClick={this.fieldClick}>
        <div className="field-value noselect">{field}</div>
      </div>
    )
  }

  fieldClick = (event) => {
    const clickedField = event.target;
    if (clickedField.disabled) {
      console.log("This field is disabled");
    } else {
      const fieldIndex = Number(clickedField.getAttribute("field-index"));
      const rowIndex = Number(clickedField.parentElement.getAttribute("row-index"));
      // console.log(rowIndex + ", " + fieldIndex);
      if (typeof fieldIndex === "number" && typeof rowIndex === "number") {
        let newGameStatus = this.state.gameStatus;
        newGameStatus[rowIndex][fieldIndex] = this.activePlayerSymbol();
        this.setState({
          gameStatus: newGameStatus,
        }, this.postProcessingClick)
        clickedField.disabled = true;
      } else {
        console.log("Something went wrong with the indexes.")
      }
    }
  }

  postProcessingClick = () => {
    this.checkWin();
    this.togglePlayer();
  }

  togglePlayer = () => {
    let newActive = 0
    if (this.state.activePlayer === 1) {
      newActive = 2;
    } else if (this.state.activePlayer === 2) {
      newActive = 1;
    }
    this.setState({
      activePlayer: newActive,
    });
  }

  checkWin = () => {
    let won = false;
    const winRow = this.checkWinRows()
    if (winRow !== null) {
      console.log("Winning row found: " + winRow);
      won = true;
    } 
    const winCol = this.checkWinColumns()
    if (winCol !== null) {
      console.log("Winning column found: " + winCol)
      won = true;
    }
    const winDiag = this.checkWinDiagonals()
    if (winDiag != null) {
      console.log("Winning diagonal found: " + winDiag);
      won = true;
    }
    if (won) {
      console.log("Winner is: " + this.state.activePlayer);
    }
  }

  checkWinRows = () => {
    for (let rowIndex = 0; rowIndex < this.state.gameStatus.length; rowIndex++) {
      let row = this.state.gameStatus[rowIndex];
      let otherValueFound = false;
      for (let fieldIndex = 0; fieldIndex < row.length; fieldIndex++) {
        let value = row[fieldIndex];
        if (!(value === this.activePlayerSymbol())) {
          otherValueFound = true;
          break;
        }
      }
      // If no other value was found, this is the winning row. Return the index.
      if (!otherValueFound) {
        return rowIndex;
      }
    }
    // If iterating through all rows without finding one where only the active players are contained
    // then this is not the winning row.
    return null;
  }

  checkWinColumns = () => {
    const columnMaxIndex = this.state.gameStatus[0].length - 1;
    for (let columnIndex = 0; columnIndex <= columnMaxIndex; columnIndex++) {
      let otherValueFound = false;
      for (let rowIndex = 0; rowIndex < this.state.gameStatus.length; rowIndex++) {
        let value = this.state.gameStatus[rowIndex][columnIndex];
        if (value !== this.activePlayerSymbol()) {
          otherValueFound = true;
          break;
        }
      }
      if (!otherValueFound) {
        return columnIndex;
      }
    }
    return null;
  }

  checkWinDiagonals = () => {
    const downDiag = [
      this.state.gameStatus[0][0],
      this.state.gameStatus[1][1],
      this.state.gameStatus[2][2],
    ]
    if (this.checkWinDiag(downDiag)) {
      return "down"
    }
    const upDiag = [
      this.state.gameStatus[2][0],
      this.state.gameStatus[1][1],
      this.state.gameStatus[0][2],
    ]
    if (this.checkWinDiag(upDiag)) {
      return "up"
    }
    return null;
  }

  checkWinDiag = (diag) => {
    let otherValueFound = false;
    for (let value of diag) {
      if (value !== this.activePlayerSymbol()) {
        otherValueFound = true;
      }
    }
    return !otherValueFound
  }
  // TODO: Highlight winning fields

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h1>{ GAME_TITLE }</h1>
        </div>
        <div className="player-header-wrapper">
          {this.drawPlayerHead()}
        </div>
        <div className="game-wrapper">
          {this.drawGame()}
        </div>
      </div>
    );
  }
}

export default App;
