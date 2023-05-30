import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import orderReducer from './reducers/orderReducer';

const rootReducer = combineReducers({
  order: orderReducer,
  // Other reducers...
});

const store = createStore(rootReducer, applyMiddleware(thunk));

export default store;