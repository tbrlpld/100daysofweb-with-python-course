import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';


function Todo(props) {
  return (
    <div>
      {props.title} { props.completed === "true" && "✔️" }
    </div>
  )
}


class App extends Component {

  render () {
    return (
      <div className="App">
        <header className="">
          <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <span className="navbar-brand">React Todo App</span>
          </nav>
        </header>
        <div className="container">
          <div className="row">
            <div className="col">
              <Todo title="Take garbage out" completed="false" />
              <Todo title="Repair sink" completed="true" />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
