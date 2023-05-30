import { useHistory } from 'react-router-dom';
import React, { useState, useEffect } from 'react';

function Sides() {
  const history = useHistory();
  const [sides, setSides] = useState([]);

  useEffect(() => {
    fetchSides();
  }, []);

  const fetchSides = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5555/sides');
      const data = await response.json();
      setSides(data);
    } catch (error) {
      console.error('Error occurred while fetching sides:', error);
    }
  };

  const handleSideClick = (sideId) => {
    history.push(`/sides/${sideId}`);
  };

  return (
    <div>
      <h2>Main</h2>
      {sides.map((side) => (
        <button
          key={side.id}
          onClick={() => handleSideClick(side.id)}
        >
          {side.name}
        </button>
      ))}
    </div>
  );
}

export default Sides