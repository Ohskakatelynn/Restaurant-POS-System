import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';

function Addons() {
  const history = useHistory();
  const [toppings, setToppings] = useState([]);

  useEffect(() => {
    fetchToppings();
  }, []);

  const fetchToppings = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5555/toppings');
      const data = await response.json();
      setToppings(data);
    } catch (error) {
      console.error('Error occurred while fetching toppings:', error);
    }
  };

  const handleToppingClick = (ToppingId) => {
    history.push(`/ToppingByID/${ToppingId}`);
  };

  return (
    <div>
      <h2>Toppings</h2>
      {toppings.map((topping) => (
        <button
          key={topping.id}
          onClick={() => handleToppingClick(topping.id)}
        >
          {topping.name}
        </button>
      ))}
    </div>
  );
}

export default Addons;