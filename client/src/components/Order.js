import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { addToOrder } from '../actions/orderActions';


function Order() {
  const order = useSelector((state) => state.order)
  const dispatch = useDispatch();

  console.log('Order:', order);

  const handleAddToOrder = (item) => {
    dispatch(addToOrder(item));
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
      {order.map((item, index) => (
        <div key={index}>
          <h3>Item {index + 1}</h3>
          <p>Product: {item.product.name}</p>
          <p>Toppings: {item.toppings.map((topping) => topping.name).join(', ')}</p>
          <p>Side: {item.side.name}</p>
          <p>Side Toppings: {item.sideToppings.map((topping) => topping.name).join(', ')}</p>
          <hr />
        </div>
      ))}
      <button onClick={handleCompleteOrder}>Complete Order</button>
    </div>
  );
}

export default Order;