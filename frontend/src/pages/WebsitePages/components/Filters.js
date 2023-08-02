import { useState } from "react";
import { useTheme } from "@mui/material/styles";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";
import Button from "@mui/material/Button";
import FilterListIcon from "@mui/icons-material/FilterList";
import OutlinedInput from "@mui/material/OutlinedInput";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import { Typography } from "@mui/material";
import Slider from "@mui/material/Slider";

/*
  Another Filtering component but this one is a dialog in case we wanna change the filters to dialog
*/

const ITEM_HEIGHT = 48;
const ITEM_PADDING_TOP = 8;
const MenuProps = {
  PaperProps: {
    style: {
      maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
      width: 250,
    },
  },
};

const rating = ["Trusted", "Not Trusted", "4.5⬆", "4.5⬇"];

function getStyles(name, personName, theme) {
  return {
    fontWeight:
      personName.indexOf(name) === -1
        ? theme.typography.fontWeightRegular
        : theme.typography.fontWeightMedium,
  };
}

function Filters() {
  const theme = useTheme();
  const [selectStores, setStores] = useState([]);
  const [selectRating, setRating] = useState([]);
  const dispatch = useDispatch();
  const storeList = useSelector((state) => state.storeList);
  const { stores } = storeList;

  useEffect(() => {
    dispatch(listStores());
  }, [dispatch]);

  const storesHandleChange = (event) => {
    const {
      target: { value },
    } = event;
    setStores(
      // On autofill we get a stringified value.
      typeof value === "string" ? value.split(",") : value
    );
  };

  const ratingHandleChange = (event) => {
    const {
      target: { value },
    } = event;
    setRating(
      // On autofill we get a stringified value.
      typeof value === "string" ? value.split(",") : value
    );
  };

  const [open, setOpen] = useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleSave = () => {};

  return (
    <>
      <Button variant="text" sx={{ marginTop: 5, width: "15%" }} onClick={handleClickOpen}>
        <FilterListIcon />
        Filters
      </Button>
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>Filters</DialogTitle>
        <DialogContent>
          <DialogContentText>Select the Wanted applied Filters</DialogContentText>
          <FormControl sx={{ m: 1, width: 300, mt: 3 }}>
            <Typography>Stores:</Typography>
            <Select
              multiple
              displayEmpty
              value={selectStores}
              onChange={storesHandleChange}
              input={<OutlinedInput />}
              renderValue={(selected) => {
                if (selected.length === 0) {
                  return <em>Select Stores...</em>;
                }

                return selected.join(", ");
              }}
              MenuProps={MenuProps}
              inputProps={{ "aria-label": "Without label" }}
              sx={{ height: 50 }}
            >
              <MenuItem disabled value="">
                <em>Stores</em>
              </MenuItem>
              {stores.map((name) => (
                <MenuItem key={name} value={name} style={getStyles(name, selectStores, theme)}>
                  {name}
                </MenuItem>
              ))}
            </Select>
            <Typography>Price:</Typography>
            <Slider defaultValue={50} aria-label="Default" valueLabelDisplay="auto" />

            <Typography>Rating:</Typography>
            <Select
              multiple
              displayEmpty
              value={selectRating}
              onChange={ratingHandleChange}
              input={<OutlinedInput />}
              renderValue={(selected) => {
                if (selected.length === 0) {
                  return <em>Select Rating...</em>;
                }

                return selected.join(", ");
              }}
              MenuProps={MenuProps}
              inputProps={{ "aria-label": "Without label" }}
              sx={{ height: 50 }}
            >
              <MenuItem disabled value="">
                <em>Rating</em>
              </MenuItem>
              {rating.map((name) => (
                <MenuItem key={name} value={name} style={getStyles(name, selectRating, theme)}>
                  {name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={handleSave}>Save</Button>
        </DialogActions>
      </Dialog>
    </>
  );
}

export default Filters;
