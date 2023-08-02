/*
    Fetching a list of stores from the backend.
    props: none
    returns : 3 cases 
      1.) Request : will dispatch that the request is still in progress
      2.) Success : it will return payload containing Array containing the stores.
      2.) Failure : it will return payload containing error and error message.
*/
import axios from "axios";
import {
  STORES_LIST_REQUEST,
  STORES_LIST_SUCCESS,
  STORES_LIST_FAIL,
} from "../Constants/listStoresConstants";

const listStores = () => async (dispatch) => {
  try {
    dispatch({ type: STORES_LIST_REQUEST });
    const { data } = await axios.get(`https://marketi-ps-caab34e05b6a.herokuapp.com/api/stores`);

    dispatch({
      type: STORES_LIST_SUCCESS,
      payload: data,
    });
  } catch (error) {
    dispatch({
      type: STORES_LIST_FAIL,
      payload:
        error.response && error.response.data.message ? error.response.data.message : error.message,
    });
  }
};

export default listStores;
