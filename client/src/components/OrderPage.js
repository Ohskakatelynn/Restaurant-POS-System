import React from 'react';
import Order from './Order';
import { useLocation } from 'react-router-dom';

function OrderPage({ orderItems }) {
  const location = useLocation();
  const order = location.state.order;

  return (
    <div>
      <h2>Order Page</h2>
      <Order orderItems={orderItems} />
    </div>
  );
}

export default OrderPage;