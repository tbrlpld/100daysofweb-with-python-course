import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';

const axios = require("axios")

const TODO_ENDPOINT = "https://jsonplaceholder.typicode.com/todos"

function Todo(props) {
  return (
    <div className="list-group-item list-group-item-action">
      { props.title } { props.completed === true && "✔️" }
    </div>
  )
}


class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      allTodos: [],
    };
    this.displayTodos = this.displayTodos.bind(this);
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

  displayTodos() {
    const todos_list_elements = this.state.allTodos.map(
      (todo, index) => {
        return (<Todo title={todo.title} completed={todo.completed} key={index} />);
      }
    );
    const todos = (<div>{todos_list_elements}</div>);
    return todos;
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
        <div className="container my-4">
          <div className="row">
            <div className="col">
              { this.displayTodos() }
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
