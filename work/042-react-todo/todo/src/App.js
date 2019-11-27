import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';

const axios = require("axios")

const TODO_ENDPOINT = "https://jsonplaceholder.typicode.com/todos"

function Todo(props) {
  return (
    <div>
      {props.title} { props.completed === "true" && "✔️" }
    </div>
  )
}


class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      allTodos: [],
    }
  }

  componentDidMount() {
    axios.get(TODO_ENDPOINT)
      .then(response => {
        this.setState({
          allTodos: response.data,
        })
        // console.log(this.state.allTodos)
      })
      .catch(error => {
        console.log(error)
      });
  }

  render () {
    return (
      <div className="App">
        <header className="">
          <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <span className="navbar-brand">
              <img src={logo} alt="React Logo" width="32px"/>
              React Todo App
            </span>
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
