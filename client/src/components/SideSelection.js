import React from 'react';

function SideSelection({ itemId, side, onSelect }) {
  return (
    <div>
      <h4>Select Side:</h4>
      <select value={side} onChange={(e) => onSelect(itemId, e.target.value)}>
        <option value="">None</option>
        <option value="Fries">Fries</option>
        <option value="Salad">Salad</option>
        <option value="Soup">Soup</option>
      </select>
    </div>
  );
}

export default SideSelection;