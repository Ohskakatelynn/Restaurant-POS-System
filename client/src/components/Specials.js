import React from "react"
import { useHistory } from 'react-router-dom';

function Specials() {
    const history = useHistory();
  
    const handleButtonClick = (route) => {
      history.push(route);
    };
  
    return (
      <div>
        <h2>Specials</h2>
        <button onClick={() => handleButtonClick('/Specials315')}>3/15 Meal</button>
        <button onClick={() => handleButtonClick('/Specialsbogodrinks')}>BOGO 1/2 Off Drinks</button>
        <button onClick={() => handleButtonClick('/Specialstuesday')}>Tuesday Special</button>
        <button onClick={() => handleButtonClick('/Specialsfriday')}>Friday D8 Night</button>
      </div>
    );
  }
  
  export default Specials;