import axios from "axios";
import {
  STORES_LIST_REQUEST,
  STORES_LIST_SUCCESS,
  STORES_LIST_FAIL,
} from "../Constants/listStoresConstants";

const listStores = () => async (dispatch) => {
  try {
    dispatch({ type: STORES_LIST_REQUEST });
    const { data } = await axios.get(`http://127.0.0.1:8000/api/stores`);

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