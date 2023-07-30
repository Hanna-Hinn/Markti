import axios from "axios";
import {
  REVIEW_LIST_REQUEST,
  REVIEW_LIST_SUCCESS,
  REVIEW_LIST_FAIL,
} from "../Constants/reviewConstants";

const listReviews = () => async (dispatch) => {
  try {
    dispatch({ type: REVIEW_LIST_REQUEST });
    const { data } = await axios.get(
      `http://marketi-ps-caab34e05b6a.herokuapp.com/api/top-reviews`
    );

    dispatch({
      type: REVIEW_LIST_SUCCESS,
      payload: data,
    });
  } catch (error) {
    dispatch({
      type: REVIEW_LIST_FAIL,
      payload:
        error.response && error.response.data.message ? error.response.data.message : error.message,
    });
  }
};

export default listReviews;
