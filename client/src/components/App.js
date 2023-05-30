import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from '../store';
import LoginFrontPage from './LoginFrontPage';
import FrontPage from './FrontPage';
import Specials from './Specials';
import Main from './Main';
import Appetizers from './Appetizers';
import Addons from './Add-ons';
import AlcoholicDrinks from './Alcoholic Drinks';
import Drinks from './Drinks';
import Kids from './Kids';
import Kitchen from './Kitchen';
import ProductByID from './ProductByID';
import Sides from './Sides';
import Order from './Order';
import ProductDetail from './ProductDetail';

function App() {
  return (
    <Provider store={store}>
      <Router>
        <Switch>
          <Route exact path="/" component={LoginFrontPage} />
          <Route exact path="/FrontPage" component={FrontPage} />
          <Route exact path="/Specials" component={Specials} />
          <Route exact path="/Main" component={Main} />
          <Route exact path="/Appetizers" component={Appetizers} />
          <Route exact path="/Addons" component={Addons} />
          <Route exact path="/AlcoholicDrinks" component={AlcoholicDrinks} />
          <Route exact path="/Drinks" component={Drinks} />
          <Route exact path="/Kids" component={Kids} />
          <Route exact path="/Kitchen" component={Kitchen} />
          <Route exact path="/ProductByID" component={ProductByID} />
          <Route exact path="/Sides" component={Sides} />
          <Route path="/product/:productId" component={ProductDetail} />
          <Route path="/order" component={Order} />
        </Switch>
      </Router>
    </Provider>
  );
}

export default App;