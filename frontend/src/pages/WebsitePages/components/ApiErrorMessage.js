import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState } from "react";
import PropTypes from "prop-types";
import Chip from "@mui/material/Chip";
import Container from "@mui/material/Container";
import CheckCircleIcon from "@mui/icons-material/CheckCircle";
import CancelIcon from "@mui/icons-material/Cancel";
import Typography from "@mui/material/Typography";
import listStores from "../actions/listStoresActions";

/*
  This component will display a store and a check or error icon in Chip
  helping the user see which stores returned products.
  
  props:
    1.) emptyApis (Array of String): list of the stores that did not return products
*/

function ApiErrorMessage({ emptyApis }) {
  const [storeListCheck, setStoreListCheck] = useState([]);
  const dispatch = useDispatch();
  const storeList = useSelector((state) => state.storeList);
  const { error, stores } = storeList;

  useEffect(() => {
    dispatch(listStores());
    setStoreListCheck([]);
    stores.forEach((store) => {
      if (emptyApis.includes(store.name)) {
        setStoreListCheck((current) => [...current, { name: store.name, check: false }]);
      } else {
        setStoreListCheck((current) => [...current, { name: store.name, check: true }]);
      }
    });
  }, [dispatch]);

  return (
    <>
      {!error && (
        <Container
          sx={{ display: "flex", gap: "3px", alignItems: "baseline", padding: "0px !important" }}
        >
          <Typography variant="caption" display="block" gutterBottom>
            Stores :
          </Typography>
          {storeListCheck.map((item) => (
            <Chip
              key={item.name}
              label={
                <>
                  {item.name}
                  {item.check ? <CheckCircleIcon color="success" /> : <CancelIcon color="error" />}
                </>
              }
              variant="outlined"
            />
          ))}
        </Container>
      )}
    </>
  );
}

export default ApiErrorMessage;

ApiErrorMessage.defaultProps = {
  emptyApis: [],
};

ApiErrorMessage.propTypes = {
  emptyApis: PropTypes.arrayOf(PropTypes.string),
};
