export const ADD_TO_ORDER = 'ADD_TO_ORDER';
export const RESET_ORDER = 'RESET_ORDER';
export const REMOVE_FROM_ORDER = 'REMOVE_FROM_ORDER';

export const addToOrder = (item) => ({
  type: ADD_TO_ORDER,
  payload: item,
});

export const resetOrder = () => ({
  type: RESET_ORDER,
});

export const removeFromOrder = (index) => ({
  type: REMOVE_FROM_ORDER,
  payload: index,
});