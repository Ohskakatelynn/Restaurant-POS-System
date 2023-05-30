import { ADD_TO_ORDER, RESET_ORDER, REMOVE_FROM_ORDER } from '../actions/orderActions';


const initialState = [];

const orderReducer = (state = initialState, action) => {
  switch (action.type) {
    case ADD_TO_ORDER:
      return [...state, action.payload];
    case RESET_ORDER:
      return initialState;
    case REMOVE_FROM_ORDER:
      const index = action.payload;
      return state.filter((item, i) => i !== index);
    default:
      return state;
  }
};

export default orderReducer;