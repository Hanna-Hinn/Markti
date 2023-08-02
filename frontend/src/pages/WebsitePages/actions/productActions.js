/*
    Fetching a list of products from the backend. And extract the max price of all prices.
    props: 
      1.) keyword : thee word that the user searches for.
      2.) sort : specifies what kind of sort we wanna sort the data.
      3.) displayCurrency : specifies what currency the user wants the data's price in. 
    
    returns : 3 cases 
      1.) Request : will dispatch that the request is still in progress
      2.) Success : it will return payload containing data, maxPrice, apiError, apiEmpty. 
      2.) Failure : it will return payload containing error and error message.
    
    returns States : 
      1.) Type (CONSTANT): type of the action
      2.) payload (list): if the keyword empty it will return empty array, 
                    if the request is success then it will array of products,
                    if the request fails it returns error.
      3.) maxPrice (number): it's the max price extracted from the list of products.
      4.) apiError (list): it's a list of the APIs that faced error in the backend.
      5.) apiEmpty (list): it's a list of the APIs that returned no products to the front.
*/

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
