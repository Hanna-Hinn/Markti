import axios from "axios";
import {
  PRODUCT_LIST_REQUEST,
  PRODUCT_LIST_SUCCESS,
  PRODUCT_LIST_FAIL,
} from "../Constants/productConstants";

const listProducts = (keyword, sort, displayCurrency) => async (dispatch) => {
  try {
    dispatch({ type: PRODUCT_LIST_REQUEST });
    if (keyword === "" || keyword === null || keyword === undefined) {
      dispatch({
        type: PRODUCT_LIST_SUCCESS,
        payload: [],
        maxPrice: 100,
        apiError: "",
        apiEmpty: ["Amazon", "AliExpress", "Ebay", "Shein"],
      });
    } else {
      const { data } = await axios.get(
        `https://marketi-ps-caab34e05b6a.herokuapp.com/api/start/?sortType=${sort.type}&keyword=${keyword}&storeList=Amazon,AliExpress,Ebay,Shein&sortAscending=${sort.asceOrDesc}&currencyType=${displayCurrency}`
      );

      const max = Math.max(...data.results.map((item) => item.product_price));

      data.results.forEach((product) => {
        if (product.product_rating > 5) {
          product.product_rating = Math.round(product.product_rating / 20); // eslint-disable-line no-param-reassign
        }
      });

      dispatch({
        type: PRODUCT_LIST_SUCCESS,
        payload: data.results,
        maxPrice: max,
        apiError: data.error,
        apiEmpty: data.empty,
      });
    }
  } catch (error) {
    dispatch({
      type: PRODUCT_LIST_FAIL,
      payload:
        error.response && error.response.data.message ? error.response.data.message : error.message,
    });
  }
};

export default listProducts;
