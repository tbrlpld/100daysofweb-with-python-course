import React, { Component } from 'react';
import logo from './logo.svg';
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
          <span className="source-link"> (<a href={ props.link } target="_blank">Source</a>)</span>
        }
      </p>
      <pre>{props.code}</pre>
      {
        props.share_link &&
        <p className="share-link">
          <a href={ props.share_link } target="_blank"><img src={ TWITTER_ICON } alt="Twitter logo" /></a>
        </p>
      }
    </div>
  );
}


class App extends Component {
  render () {
    return (
      <div className="App">
        <h1>{ PROJECT_NAME } <small>from PyBites</small></h1>
        <Tip tip="Just some text" link="https://example.com/" code="a + b \n c" share_link="http://example.com/share"/>
      </div>
    );
  }
}


export default App;
