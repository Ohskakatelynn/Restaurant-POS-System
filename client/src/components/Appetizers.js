import React from "react"
import { useHistory } from 'react-router-dom';

function Appetizers() {

    const history = useHistory();
  
    const handleButtonClick = (route) => {
      history.push(route);
    };
  
    return (
      <div>
        <h2>Appetizers</h2>
        <button onClick={() => handleButtonClick('/')}>Buffalo Wings</button>
        <button onClick={() => handleButtonClick('/')}>Chips & Salsa</button>
        <button onClick={() => handleButtonClick('/')}>Quad Dip Combo</button>
        <button onClick={() => handleButtonClick('/')}>Fried Okra</button>
        <button onClick={() => handleButtonClick('/')}>Cheesy Garlic Breadsticks</button>
        <button onClick={() => handleButtonClick('/')}>Bacon Mini Sliders</button>
      </div>
    );
  }
export default Appetizers