import React, { Component } from 'react';
import './App.css';

const axios = require("axios");

const PROJECT_NAME = "Python Tips"
const TWITTER_ICON = "https://codechalleng.es/static/img/icon-twitter.png"
const TIPS_ENDPOINT = "http://127.0.0.1:8000/api/"

function Tip(props) {
  return (
    <div className="tip">
      <p>
        {props.tip}
        {
          props.link &&
          <span className="source-link"> (<a href={ props.link } target="_blank" rel="noopener noreferrer">Source</a>)</span>
        }
      </p>
      <pre>{props.code}</pre>
      {
        props.share_link &&
        <p className="share-link">
          <a href={ props.share_link } target="_blank" rel="noopener noreferrer"><img src={ TWITTER_ICON } alt="Twitter logo" /></a>
        </p>
      }
    </div>
  );
}


class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      origTips: [],
      showTips: [],
      filterStr: "",
    };
    this.onFilterStringChange = this.onFilterStringChange.bind(this);
    this.displayTips = this.displayTips.bind(this);
  }


  componentDidMount() {
    console.log("Component did mount!");
    axios.get(TIPS_ENDPOINT)
      .then(response => {
        console.log(response.data);
        this.setState({
          origTips: response.data,
          showTips: response.data,
        });
      })
      .catch(error => {
        console.log(error);
      })
  }

  onFilterStringChange(event) {
    const inputValue =  event.target.value
    const filterStr = inputValue ? inputValue.toLowerCase() : "" ;  // If inputValue then inpuValue.toLowerCase, else "".
    this.setState({
      filterStr: filterStr,
      showTips: this.filterShowTips(filterStr),
    });
  }

  filterShowTips(filterStr) {
    let filteredTips = []
    const allTips = this.state.origTips
    for (const tip of allTips) {
      if (
        ( tip.tip && tip.tip.toLowerCase().includes(filterStr) ) 
        || ( tip.code && tip.code.toLowerCase().includes(filterStr) )
      ) {
        filteredTips.push(tip)
      }
    }
    return filteredTips;
  }

  displayTips() {
    const tipsDisplay = this.state.showTips.map(
      (tip, index) => {
        return (<Tip {...tip} key={index} filterStr={this.state.filterStr} />)
      }
    )
    return tipsDisplay
  }

  render () {
    return (
      <div className="App">
        <h1>{ PROJECT_NAME } <small>from PyBites</small></h1>
        <input type="text" name="search" onChange={this.onFilterStringChange}/>
        <hr/>
        <div className="tips">
          { this.displayTips() }
        </div>
      </div>
    );
  }
}


export default App;
