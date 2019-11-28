import React, {Component} from 'react';
import update from "react-addons-update"
import logo from './logo.svg';
import './App.css';

const axios = require("axios")

const TODO_ENDPOINT = "https://jsonplaceholder.typicode.com/todos"


class Todo extends Component {

  constructor(props) {
    super(props);
    this.state = {
      title: props.title,
      completed: props.completed || false,
    };
    this.toggleStatusOnClick = this.toggleStatusOnClick.bind(this);
  }

  toggleStatusOnClick(event) {
    const initial_status = this.state.completed;
    if (initial_status === true) {
      this.setState({completed: false});
    } else {
      this.setState({completed: true});
    };
  }

  render() {
    return (
      <div className={"list-group-item list-group-item-action text-capitalize " + ((this.state.completed === true) ? "text-muted" : "")} onClick={this.toggleStatusOnClick}>
        <span className={(this.state.completed === true) ? "text-strike-through" : ""}>{ this.state.title }</span> { this.state.completed === true && "✔️" }
      </div>
    )
  }
}

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      allTodos: []
    };
    this.displayTodos = this.displayTodos.bind(this);
    this.addNewItem = this.addNewItem.bind(this);
  }

  componentDidMount() {
    console.log("Did mount")
    axios.get(TODO_ENDPOINT)
      .then(response => {
        this.setState({
          allTodos: response.data.slice(0,10),
        })
      })
      .catch(error => {
        console.log(error)
      });
  }

  displayTodos() {
    const todos_list_elements = this.state.allTodos.map(
      (todo, index) => {
        // console.log(todo.title);
        return (<Todo title={todo.title} completed={todo.completed} key={index} />);
      }
    );
    const todos = (<div>{todos_list_elements}</div>);
    return todos;
  }

  addNewItem(event) {
    const addTodoInput = document.getElementById("input-add-new-todo");
    if (addTodoInput.value) {
      const newItem = {
        title: addTodoInput.value,
        completed: false,
      };
      addTodoInput.value = "";

      const initialTodoObjects = this.state.allTodos;
      const todoObjects = update(initialTodoObjects, {$push: [newItem]});  
      this.setState({
        allTodos: todoObjects,
      });
    }
  }

  render() {
    console.log("Rendering app");
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
          <div className="row mb-4">
            <div className="col">
              <div className="input-group">
                <input id="input-add-new-todo" className="form-control" type="text" placeholder="Add something to do..." />
                <div className="input-group-append">
                  <input className="btn btn-outline-primary" type="submit" value="Add" onClick={this.addNewItem}/>
                </div>
              </div>
            </div>
          </div>
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
