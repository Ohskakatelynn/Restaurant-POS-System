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
  const parsedOrder = storedOrder ? JSON.parse(storedOrder) : {};

  const handlePostOrder = async () => {
    try {
      // Step 1: Post ProductWithTopping
      const productWithToppingResponse = await fetch('http://127.0.0.1:5555/productwithtoppings', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(parsedOrder.productWithTopping), // Replace `parsedOrder.productWithTopping` with the correct data
      });
  
      if (!productWithToppingResponse.ok) {
        console.error('Failed to post ProductWithTopping to the backend');
        return;
      }
  
      const productWithToppingData = await productWithToppingResponse.json();
      const productWithToppingId = productWithToppingData.id;
  
      // Step 2: Post SideWithTopping
      const sideWithToppingResponse = await fetch('http://127.0.0.1:5555/sidewithtoppings', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(parsedOrder.sideWithTopping), // Replace `parsedOrder.sideWithTopping` with the correct data
      });
  
      if (!sideWithToppingResponse.ok) {
        console.error('Failed to post SideWithTopping to the backend');
        return;
      }
  
      const sideWithToppingData = await sideWithToppingResponse.json();
      const sideWithToppingId = sideWithToppingData.id;
  
      // Step 3: Create OrderItem
      const orderItemResponse = await fetch('http://127.0.0.1:5555/orderitems', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          product_with_topping_id: productWithToppingId,
          side_with_topping_id: sideWithToppingId,
          mealprice: parsedOrder.mealprice, // Replace `parsedOrder.mealprice` with the correct value
          status: parsedOrder.status, // Replace `parsedOrder.status` with the correct value
        }),
      });
  
      if (!orderItemResponse.ok) {
        console.error('Failed to create OrderItem');
        return;
      }
  
      const orderItemData = await orderItemResponse.json();
      const orderItemId = orderItemData.id;
  
      // Step 4: Create Order
      const orderResponse = await fetch('http://127.0.0.1:5555/orders', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          order_item_id: orderItemId,
          ticketnumbers_id: parsedOrder.ticketnumbers_id, // Replace `parsedOrder.ticketnumbers_id` with the correct value
          total_price: parsedOrder.total_price, // Replace `parsedOrder.total_price` with the correct value
          table_id: parsedOrder.table_id, // Replace `parsedOrder.table_id` with the correct value
        }),
      });
  
      if (orderResponse.ok) {
        console.log('Order posted successfully!');
        // Perform any additional actions after successfully posting the order
      } else {
        console.error('Failed to post order to the backend');
      }
    } catch (error) {
      console.error('Error occurred while posting order:', error);
    }
  };

  return (
    <div>
      <h2>Order Summary</h2>
      {Array.isArray(order) && order.length > 0 ? (
        <ul>
          {order.map((item, index) => (
            <li key={index}>
              <p>Product: {item.product && item.product.name}</p>
              <p>Toppings: {item.toppings && item.toppings.map((topping) => topping.name).join(', ')}</p>
              <p>Side: {item.side && item.side.name}</p>
              <p>Side Toppings: {item.sideToppings && item.sideToppings.map((topping) => topping.name).join(', ')}</p>
              <button onClick={() => handleRemoveFromOrder(index)}>Remove</button>
            </li>
          ))}
        </ul>
      ) : (
        <p>No items in the order.</p>
      )}
      <button onClick={handlePostOrder}>Add Order to Backend</button>
    </div>
  );
}

export default Order;