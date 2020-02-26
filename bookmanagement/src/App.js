import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
//import { HomePage } from "./HomePage";
import Books from "./BookCard"
import Header from "./Header"

/*
 * React's Component ( Main )
 */
class App extends Component {

  /*
   * Field
   */
  // web api
  api_url = "http://localhost:80/list";

  // state has book list.
  state = {
    books: []
  }

  /**
   * Component#componentDidMount()
   * マウント（画面上に表示)が終わった後呼び出されるメソッド
   */
  componentDidMount() {
    /*
    * this.intervalId = setInterval()
    */

    // API Callして得たJSONを自クラスにsetStateする．
    fetch(this.api_url).then(res => {
      return res.json();
    }).then((data) => {
      this.setState({ books: data })
    }).catch(console.log)
  }

  /**
   * Component#render()
   * マウント(画面上に表示)する前に呼び出される
   */
  render() {
    return (
      // JSX to render goes here..
      <Router>
        <div>
          <Header />
          <Switch>
            <Route exact path="/">
              <div className="flex mb-4 justify-center items-center flex-wrap" id="CardView1">
                <Books books={this.state.books} id="Books1" />
              </div>
            </Route>
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;
