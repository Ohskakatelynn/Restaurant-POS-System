import React from 'react';
import { BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import LoginFrontPage from "./LoginFrontPage"

// Components for each route
// const Home = () => <h1>Home Page</h1>;

function App() {

  return (
      <Router>
        <Switch>
          <Route path="/">
            <LoginFrontPage/>
          </Route>
        </Switch>
      </Router>
  
  
  
    )
};

export default App;
