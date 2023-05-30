import React from 'react';
import { useHistory } from 'react-router-dom';

function FrontPage() {
  const history = useHistory();

  const handleButtonClick = (route) => {
    history.push(route);
  };

  return (
    <div>
      <h2>Front Page</h2>
      <button onClick={() => handleButtonClick('/Specials')}>Specials</button>
      <button onClick={() => handleButtonClick('/Main')}>Main</button>
      <button onClick={() => handleButtonClick('/Appetizers')}>Appetizers</button>
      <button onClick={() => handleButtonClick('/Sides')}>Sides</button>
      <button onClick={() => handleButtonClick('/Addons')}>Addons</button>
      <button onClick={() => handleButtonClick('/Kids')}>Kids</button>
      <button onClick={() => handleButtonClick('/AlcoholicDrinks')}>AlcoholicDrinks</button>
      <button onClick={() => handleButtonClick('/Drinks')}>Drinks</button>
      <div><button onClick={() => history.push('/order')}>View Order Summary</button></div>
    </div>
    
  );
}

export default FrontPage;