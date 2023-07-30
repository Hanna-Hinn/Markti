import PropTypes from "prop-types";
import { useDispatch, useSelector } from "react-redux";
import { Box, Button, FormControl } from "@mui/material";
import FilterAltIcon from "@mui/icons-material/FilterAlt";
import { useState, useEffect } from "react";
import Menu from "@mui/material/Menu";
import FormGroup from "@mui/material/FormGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import FormLabel from "@mui/material/FormLabel";
import FormHelperText from "@mui/material/FormHelperText";
import Slider from "@mui/material/Slider";
import listStores from "../actions/listStoresActions";

// import TextField from "@mui/material/TextField";

function FilterButton({ setFilterState, maxPriceValue, applyFilters }) {
  const dispatch = useDispatch();
  const storeList = useSelector((state) => state.storeList);
  const { stores } = storeList;
  const minDistance = 10;
  const [ratingState, setRatingState] = useState({
    // Above4: false,
    // under4: false,
    Trusted: false,
    NotTrusted: false,
    Above4: false,
    Under4: false,
  });

  const [storeState, setStoreState] = useState({
    // Amazon: true,
    // AliExpress: true,
    // Ebay: true,
  });

  useEffect(() => {
    dispatch(listStores());
  }, [dispatch]);

  const [priceState, setPriceState] = useState([0, maxPriceValue]);
  // const [priceError, setPriceError] = useState(false);
  // const [minPrice, setMinPrice] = useState(0);
  // const [maxPrice, setMaxPrice] = useState(maxPriceValue);

  const [anchorEl, setAnchorEl] = useState(null);
  const open = Boolean(anchorEl);
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleRatingChange = (event) => {
    setRatingState({
      ...ratingState,
      [event.target.name]: event.target.checked,
    });
  };
  const handleStoreChange = (event) => {
    setStoreState({
      ...storeState,
      [event.target.name]: event.target.checked,
    });
  };

  const handlePriceChange = (event, newValue, activeThumb) => {
    if (!Array.isArray(newValue)) {
      return;
    }

    if (activeThumb === 0) {
      setPriceState([Math.min(newValue[0], priceState[1] - minDistance), priceState[1]]);
    } else {
      setPriceState([priceState[0], Math.max(newValue[1], priceState[0] + minDistance)]);
    }
  };

  // const handleMinPriceChange = (event) => {
  //   const { value } = event.target;

  //   console.log("MIN", value);
  //   if (event.value >= 0) {
  //     setPriceError(false);
  //     setMinPrice(value);
  //   } else {
  //     setPriceError(true);
  //   }
  //   console.log("MIN value", minPrice);
  // };

  // const handleMaxPriceChange = (event) => {
  //   console.log("MAX", event.value);
  //   if (event.value >= 0) {
  //     setPriceError(false);
  //     setMaxPrice(event.value);
  //   } else {
  //     setPriceError(true);
  //   }
  // };

  useEffect(() => {
    setPriceState([0, maxPriceValue]);
  }, [maxPriceValue]);

  // const { Amazon, AliExpress, Ebay, Shein } = storeState;
  // const { Above4, under4, Trusted, NotTrusted } = ratingState;
  const { Trusted, NotTrusted, Above4, Under4 } = ratingState;

  const storeError = Object.keys(storeState).filter((v) => v).length < 1;

  const handleSaveFilters = () => {
    if (!storeError) {
      const storesSave = Object.keys(storeState)
        .map((key) => {
          if (storeState[key]) {
            return key;
          }
          return undefined;
        })
        .filter((element) => element !== undefined);

      const rating = Object.keys(ratingState)
        .map((key) => {
          if (ratingState[key]) {
            return key;
          }
          return undefined;
        })
        .filter((element) => element !== undefined);

      setFilterState({
        rating,
        stores: storesSave,
        price: priceState,
      });
      applyFilters();
      setAnchorEl(null);
    }
  };

  return (
    <>
      <Button
        variant="text"
        sx={{ marginTop: 5, width: "15%" }}
        aria-controls={open ? "basic-menu" : undefined}
        aria-haspopup="true"
        aria-expanded={open ? "true" : undefined}
        onClick={handleClick}
      >
        <FilterAltIcon />
        Filters
      </Button>
      <Menu
        id="basic-menu"
        anchorEl={anchorEl}
        open={open}
        onClose={handleClose}
        MenuListProps={{
          "aria-labelledby": "basic-button",
        }}
      >
        <Box sx={{ display: "flex", flexWrap: "wrap" }}>
          <Box>
            <FormControl
              required
              error={storeError}
              component="fieldset"
              sx={{ m: 3 }}
              variant="standard"
            >
              <FormLabel component="legend">Stores</FormLabel>
              <FormGroup>
                {stores &&
                  stores.map((item) => (
                    <FormControlLabel
                      key={item.name}
                      control={
                        <Checkbox
                          checked={storeState[`${item.name}`]}
                          onChange={handleStoreChange}
                          name={item.name}
                        />
                      }
                      label={item.name}
                    />
                  ))}
                {/* <FormControlLabel
                  control={<Checkbox checked={Amazon} onChange={handleStoreChange} name="Amazon" />}
                  label="Amazon"
                />
                <FormControlLabel
                  control={<Checkbox checked={Ebay} onChange={handleStoreChange} name="Ebay" />}
                  label="Ebay"
                />
                <FormControlLabel
                  control={
                    <Checkbox checked={AliExpress} onChange={handleStoreChange} name="AliExpress" />
                  }
                  label="AliExpress"
                /> */}
              </FormGroup>
              <FormHelperText>Please Pick AtLeast One!</FormHelperText>
            </FormControl>
          </Box>

          <Box>
            <FormControl component="fieldset" sx={{ m: 3 }} variant="standard">
              <FormLabel component="legend">Rating</FormLabel>
              <FormGroup>
                <FormControlLabel
                  control={
                    <Checkbox checked={Above4} onChange={handleRatingChange} name="Above4" />
                  }
                  label="4⬆"
                />
                <FormControlLabel
                  control={
                    <Checkbox checked={Under4} onChange={handleRatingChange} name="Under4" />
                  }
                  label="4⬇"
                />
                <FormControlLabel
                  control={
                    <Checkbox checked={Trusted} onChange={handleRatingChange} name="Trusted" />
                  }
                  label="Trusted"
                />
                <FormControlLabel
                  control={
                    <Checkbox
                      checked={NotTrusted}
                      onChange={handleRatingChange}
                      name="NotTrusted"
                    />
                  }
                  label="Not Trusted"
                />
              </FormGroup>
            </FormControl>
          </Box>

          <Box
            sx={{
              m: 3,
              flexBasis: "100%",
            }}
          >
            <FormControl component="fieldset" sx={{ m: 3, width: "90%" }} variant="standard">
              <FormLabel component="legend">Price</FormLabel>
              <Slider
                value={priceState}
                onChange={handlePriceChange}
                valueLabelDisplay="auto"
                sx={{ width: "100%" }}
                disableSwap
                min={0}
                max={maxPriceValue}
              />
              {/* <Box
                component="span"
                sx={{ display: "flex", m: 3, width: "100%", justifyContent: "space-between" }}
              >
                <TextField
                  error={priceError}
                  value={minPrice}
                  onChange={handleMinPriceChange}
                  sx={{
                    width: "fit-content",
                    height: 50,
                  }}
                />
                <TextField
                  error={priceError}
                  value={maxPrice}
                  onChange={handleMaxPriceChange}
                  sx={{
                    width: "fit-content",
                    height: 50,
                  }}
                />
              </Box> */}
              {`Price from ${priceState[0]} to ${priceState[1]}`}
            </FormControl>
          </Box>
        </Box>
        <Box sx={{ display: "flex", bottom: 0, right: 0 }}>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={handleSaveFilters}>Save</Button>
        </Box>
      </Menu>
    </>
  );
}

export default FilterButton;

FilterButton.defaultProps = {
  maxPriceValue: 100,
};

FilterButton.propTypes = {
  setFilterState: PropTypes.func.isRequired,
  maxPriceValue: PropTypes.number,
  applyFilters: PropTypes.func.isRequired,
};
