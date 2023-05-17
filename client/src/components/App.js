import React from 'react';
import { BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import LoginFrontPage from "./LoginFrontPage"
import FrontPage from "./FrontPage"
import Specials from "./Specials"
import Main from "./Main"
import Appetizers from "./Appetizers"
import Addons from "./Add-ons"
import AlcoholicDrinks from "./Alcoholic Drinks"
import Drinks from "./Drinks"
import Kids from "./Kids"
import Kitchen from "./Kitchen"
import ProductByID from "./ProductByID"
import Sides from "./Sides"


function App() {

  return (
      <Router>
        <Switch>
          <Route path="/">
            <LoginFrontPage/>
          </Route>
          <Route path="/FrontPage">
            <FrontPage/>
          </Route>
          <Route path="/Specials">
            <Specials/>
          </Route>
          <Route path="/Main">
            <Main/>
          </Route>
          <Route path="/Appetizers">
            <Appetizers/>
          </Route>
          <Route path="/Sides">
            <Sides/>
          </Route>
          <Route path="/AddOns">
            <Addons/>
          </Route>
          <Route path="/Kids">
            <Kids/>
          </Route>
          <Route path="/AlcoholicDrinks">
            <AlcoholicDrinks/>
          </Route>
          <Route path="/Drinks">
            <Drinks/>
          </Route>
          <Route path="/ProductByID">
            <ProductByID/>
          </Route>
          <Route path="/Kitchen">
            <Kitchen/>
          </Route>
        </Switch>
      </Router>
  
  
  
    )
};

export default App;
