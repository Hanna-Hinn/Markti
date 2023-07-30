import { FILTER_REQUEST, FILTER_SUCCESS } from "../Constants/filterConstants";

const filterListReducers = (state = { filteredProducts: [] }, action) => {
  switch (action.type) {
    case FILTER_REQUEST:
      return { filteredProducts: [] };
    case FILTER_SUCCESS:
      return {
        filteredProducts: action.payload,
      };
    default:
      return state;
  }
};

export default filterListReducers;
