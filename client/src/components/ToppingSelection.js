import React from 'react';

function ToppingSelection({ itemId, toppings, onToppingClick }) {
  return (
    <div>
      <h4>Select Toppings:</h4>
      {toppings.map((topping) => (
        <button key={topping.id} onClick={() => onToppingClick(itemId, topping.id)}>
          {topping.name}
        </button>
      ))}
    </div>
  );
}

export default ToppingSelection;