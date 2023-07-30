import axios from "axios";
import {
  PRODUCT_LIST_REQUEST,
  PRODUCT_LIST_SUCCESS,
  PRODUCT_LIST_FAIL,
} from "../Constants/productConstants";

const listProducts = (keyword, sort) => async (dispatch) => {
  try {
    dispatch({ type: PRODUCT_LIST_REQUEST });
    const { data } = await axios.get(
      `http://127.0.0.1:8000/api/start/?sortType=${sort.type}&keyword=${keyword}&storeList=Amazon,AliExpress,Ebay,Shein&sortAscending=${sort.asceOrDesc}`
    );

    const max = Math.max(...data.results.map((item) => item.product_price));

    dispatch({
      type: PRODUCT_LIST_SUCCESS,
      payload: data.results,
      maxPrice: max,
      apiError: data.error,
      apiEmpty: data.empty,
    });
  } catch (error) {
    dispatch({
      type: PRODUCT_LIST_FAIL,
      payload:
        error.response && error.response.data.message ? error.response.data.message : error.message,
    });
  }
};

export default listProducts;
