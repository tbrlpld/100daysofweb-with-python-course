import React, { Component } from 'react';
import './App.css';

const PROJECT_NAME = "Python Tips"
const TWITTER_ICON = "https://codechalleng.es/static/img/icon-twitter.png"

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
  }


  componentDidMount() {
    console.log("Component did mount!");
  }

  onFilterStringChange(event) {
    console.log("Filter string has changes.");
  }

  render () {
    return (
      <div className="App">
        <h1>{ PROJECT_NAME } <small>from PyBites</small></h1>
        <input type="text" name="search" onChange={this.onFilterStringChange}/>
        <hr/>
        <Tip tip="Just some text" link="https://example.com/" code="a + b \n c" share_link="http://example.com/share"/>
      </div>
    );
  }
}


export default App;
