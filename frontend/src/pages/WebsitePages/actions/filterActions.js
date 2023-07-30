import { useState } from "react";
import { FILTER_REQUEST, FILTER_SUCCESS } from "../Constants/filterConstants";

const filterList = (products, filterState) => async (dispatch) => {
  dispatch({ type: FILTER_REQUEST });
  const [data, setData] = useState([products]);
  if (filterState.rating && filterState.rating.length > 0) {
    setData(
      products.filter((product) =>
        filterState.rating.some((value) => value === product.product_rating)
      )
    );
  }
  if (filterState.stores && filterState.stores.length >= 1) {
    setData(
      products.filter((product) =>
        filterState.rating.some((value) => value === product.product_store)
      )
    );
  }

  // if (filterState.price && filterState.price.length === 2) {
  //   setData(products.filter((product) => product.product_price >= filterState.price[0]));
  //   setData(products.filter((product) => product.product_price <= filterState.price[1]));
  // }

  console.log("filter Data", data);

  dispatch({
    type: FILTER_SUCCESS,
    payload: data,
  });
};

export default filterList;
