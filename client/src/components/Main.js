import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { addToOrder, removeFromOrder } from '../actions/orderActions';

function Main() {
  const history = useHistory();
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [selectedToppings, setSelectedToppings] = useState([]);
  const [selectedSide, setSelectedSide] = useState(null);
  const [selectedSideToppings, setSelectedSideToppings] = useState([]);
  const order = useSelector((state) => state.order);
  const dispatch = useDispatch();

  const [products, setProducts] = useState([]);
  const [sides, setSides] = useState([]);
  const [toppings, setToppings] = useState([]);

  useEffect(() => {
    fetchProducts();
    fetchSides();
    fetchToppings();
  }, []);

  const fetchProducts = async () => {
    try {
      const response = await fetch('/products');
      const data = await response.json();
      setProducts(data);
    } catch (error) {
      console.error('Error occurred while fetching products:', error);
    }
  };

  const fetchSides = async () => {
    try {
      const response = await fetch('/sides');
      const data = await response.json();
      setSides(data);
    } catch (error) {
      console.error('Error occurred while fetching sides:', error);
    }
  };

  const fetchToppings = async () => {
    try {
      const response = await fetch('/toppings');
      const data = await response.json();
      setToppings(data);
    } catch (error) {
      console.error('Error occurred while fetching toppings:', error);
    }
  };

  const handleProductSelection = (product) => {
    setSelectedProduct(product);
  };

  const handleToppingSelection = (topping) => {
    setSelectedToppings((prevToppings) => {
      if (prevToppings.includes(topping)) {
        return prevToppings.filter((selectedTopping) => selectedTopping !== topping);
      } else {
        return [...prevToppings, topping];
      }
    });
  };

  const handleSideSelection = (side) => {
    setSelectedSide(side);
  };

  const handleSideToppingSelection = (topping) => {
    setSelectedSideToppings((prevToppings) => {
      if (prevToppings.includes(topping)) {
        return prevToppings.filter((selectedTopping) => selectedTopping !== topping);
      } else {
        return [...prevToppings, topping];
      }
    });
  };

  const handleAddToOrder = async () => {
    try {
      const productWithToppings = [];

      for (const selectedTopping of selectedToppings) {
        const productWithToppingResponse = await fetch('/productwithtoppings', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            product_id: selectedProduct.id,
            topping_id: selectedTopping.id,
          }),
        });

        console.log(selectedProduct.id);
        console.log(selectedTopping.id);

        const productWithToppingData = await productWithToppingResponse.json();
        productWithToppings.push(productWithToppingData);
      }

      console.log('ProductWithToppings created:', productWithToppings);

      try {
        const sideWithToppings = [];

        for (const selectedSideTopping of selectedSideToppings) {
          const sideWithToppingResponse = await fetch('/sidewithtoppings', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              side_id: selectedSide.id,
              topping_id: selectedSideTopping.id,
            }),
          });

          console.log(selectedSide.id);
          console.log(selectedSideTopping.id);

          const sideWithToppingData = await sideWithToppingResponse.json();
          sideWithToppings.push(sideWithToppingData);
        }

        console.log('SideWithToppings created:', sideWithToppings);

        const orderItems = productWithToppings.map((productWithTopping) => ({
          productWithToppingId: productWithTopping.id,
          sideId: selectedSide ? selectedSide.id : null,
          sideToppingIds: selectedSideToppings.map((topping) => topping.id),
        }));

        for (const orderItem of orderItems) {
          dispatch(addToOrder(orderItem));
        }

        history.push('/order');
      } catch (error) {
        console.error('Error occurred while creating side with toppings:', error);
      }
    } catch (error) {
      console.error('Error occurred while adding to order:', error);
    }
  };

  const handleRemoveFromOrder = (index) => {
    dispatch(removeFromOrder(index));
  };

  const handleOrderClick = () => {
    history.push('/order');
  };

  const handleClearToppings = () => {
    setSelectedToppings([]);
  };

  return (
    <div>
      {!selectedProduct && (
        <div>
          <h2>Main Page</h2>
          {products.map((product) => (
            <button key={product.id} onClick={() => handleProductSelection(product)}>
              {product.name}
            </button>
          ))}
        </div>
      )}

      {selectedProduct && (
        <div>
          <h2>Customize {selectedProduct.name}</h2>
          <p>Select toppings:</p>
          {toppings.map((topping) => (
            <button key={topping.id} onClick={() => handleToppingSelection(topping)}>
              {topping.name}
            </button>
          ))}
          <button onClick={() => setSelectedProduct(null)}>Back to Products</button>
          <button onClick={handleClearToppings}>Clear Toppings</button>
        </div>
      )}

      {selectedProduct && selectedToppings.length > 0 && !selectedSide && (
        <div>
          <h2>Select a Side</h2>
          {sides.map((side) => (
            <button key={side.id} onClick={() => handleSideSelection(side)}>
              {side.name}
            </button>
          ))}
          <button onClick={() => setSelectedToppings([])}>Back to Toppings</button>
          <button onClick={handleClearToppings}>Clear Toppings</button>
          <button onClick={() => setSelectedSide(null)}>Clear Side</button>
        </div>
      )}

      {selectedProduct && selectedToppings.length > 0 && selectedSide && (
        <div>
          <h2>Customize Side: {selectedSide.name}</h2>
          <p>Select toppings:</p>
          {toppings.map((topping) => (
            <button key={topping.id} onClick={() => handleSideToppingSelection(topping)}>
              {topping.name}
            </button>
          ))}
          <button onClick={() => setSelectedSide(null)}>Back to Sides</button>
          <button onClick={() => setSelectedSideToppings([])}>Clear Side Toppings</button>
          <button onClick={handleClearToppings}>Clear Toppings</button>
        </div>
      )}

      {selectedProduct && selectedToppings.length > 0 && selectedSide && selectedSideToppings.length > 0 && (
        <div>
          <h2>Review Order</h2>
          <p>Product: {selectedProduct.name}</p>
          <p>Toppings: {selectedToppings.map((topping) => topping.name).join(', ')}</p>
          <p>Side: {selectedSide.name}</p>
          <p>Side Toppings: {selectedSideToppings.map((topping) => topping.name).join(', ')}</p>
          <button onClick={handleAddToOrder}>Add to Order</button>
          <button onClick={() => setSelectedSide(null)}>Modify Side</button>
          <button onClick={() => setSelectedToppings([])}>Modify Toppings</button>
          <button onClick={handleClearToppings}>Clear Toppings</button>
        </div>
      )}

      <button onClick={handleOrderClick}>Go to Order</button>
    </div>
  );
}

export default Main;