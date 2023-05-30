import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

function ProductDetail() {
    const { productId } = useParams();
    const [product, setProduct] = useState(null);
    const [orderItems, setOrderItems] = useState([])
  
    useEffect(() => {
      fetchProduct();
    }, []);
  
    const fetchProduct = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:5555/products/${productId}`);
        const data = await response.json();
        setProduct(data);
      } catch (error) {
        console.error('Error occurred while fetching product:', error);
      }
    };
  
    const handleAddToOrder = () => {
      if (product) {
        const newItem = {
          id: product.id,
          name: product.name,
          price: product.price,
          toppings: [],
          side: null
        };
  
        setOrderItems((prevOrderItems) => [...prevOrderItems, newItem]);
      }
    };
  
    return (
      <div>
        {product ? (
          <div>
            <h2>{product.name}</h2>
            <p>{product.description}</p>
            <p>Price: {product.price}</p>
            <button onClick={handleAddToOrder}>Add to Order</button>
          </div>
        ) : (
          <p>Loading product...</p>
        )}
      </div>
    );
  }
export default ProductDetail;