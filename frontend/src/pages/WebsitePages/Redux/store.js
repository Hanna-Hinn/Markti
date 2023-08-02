import { createStore, combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { composeWithDevTools } from "redux-devtools-extension";
import productListReducers from "../reducers/productsReducers";
import reviewListReducers from "../reducers/reviewReducers";
import storesListReducers from "../reducers/listStoresReducers";

const reducer = combineReducers({
  productList: productListReducers,
  reviewList: reviewListReducers,
  storeList: storesListReducers,
});

const initialState = {};

const middleware = [thunk];

const store = createStore(
  reducer,
  initialState,
  composeWithDevTools(applyMiddleware(...middleware))
);

export default store;
