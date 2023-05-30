const ADD_TO_ORDER = 'ADD_TO_ORDER';
const RESET_ORDER = 'RESET_ORDER';


const initialState = [];

const orderReducer = (state = initialState, action) => {
  switch (action.type) {
    case ADD_TO_ORDER:
      return [...state, action.payload];
    case RESET_ORDER:
      return initialState;
    default:
      return state;
  }
};

export default orderReducer;