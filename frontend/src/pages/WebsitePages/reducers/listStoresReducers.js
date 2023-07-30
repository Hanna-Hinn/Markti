import {
  STORES_LIST_REQUEST,
  STORES_LIST_SUCCESS,
  STORES_LIST_FAIL,
} from "../Constants/listStoresConstants";

const storesListReducers = (state = { stores: [] }, action) => {
  switch (action.type) {
    case STORES_LIST_REQUEST:
      return { loading: true, stores: [] };
    case STORES_LIST_SUCCESS:
      return {
        loading: false,
        stores: action.payload,
      };
    case STORES_LIST_FAIL:
      return { loading: false, error: action.payload };
    default:
      return state;
  }
};

export default storesListReducers;
