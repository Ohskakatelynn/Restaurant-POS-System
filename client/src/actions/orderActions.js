export const ADD_TO_ORDER = 'ADD_TO_ORDER';
export const RESET_ORDER = 'RESET_ORDER';

export const addToOrder = (item) => ({
  type: ADD_TO_ORDER,
  payload: item,
});

export const resetOrder = () => ({
  type: RESET_ORDER,
});