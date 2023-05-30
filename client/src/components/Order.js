import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { addToOrder } from '../actions/orderActions';
import { removeFromOrder } from '../actions/orderActions';


function Order() {
  const order = useSelector((state) => state.order)
  const dispatch = useDispatch();

  console.log('Order:', order);


  const handleRemoveFromOrder = (index) => {
    dispatch(removeFromOrder(index));
  };

  useEffect(() => {
    // Save the order data to localStorage
    localStorage.setItem('order', JSON.stringify(order));
  }, [order]);

  const storedOrder = localStorage.getItem('order');
  const parsedOrder = storedOrder ? JSON.parse(storedOrder) : [];

  const handleCompleteOrder = () => {
    // TODO: Send the order data to the backend
    console.log('Sending order:', order);
    // Rest of your code...
  }

  return (
    <div>
      <h2>Order Summary</h2>
      {order.length > 0 ? (
        <ul>
          {order.map((item, index) => (
            <li key={index}>
              <p>Product: {item.product.name}</p>
              <p>Toppings: {item.toppings.map((topping) => topping.name).join(', ')}</p>
              <p>Side: {item.side.name}</p>
              <p>Side Toppings: {item.sideToppings.map((topping) => topping.name).join(', ')}</p>
              <button onClick={() => handleRemoveFromOrder(index)}>Remove</button>
            </li>
          ))}
        </ul>
      ) : (
        <p>No items in the order.</p>
      )}
    </div>
  );
}

export default Order;






