import PropTypes from "prop-types";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import ListItemText from "@mui/material/ListItemText";
import Checkbox from "@mui/material/Checkbox";

/*
  This is a Select Component

  props: 
    1.) title : specifies the label text of the select
    2.) selectedStores: specifies the selected item of the items.
    3.) handleChange: event listener function that will change the value of the selectStores if the user selects another value.
    4.) items: list of items that will be displayed for the user to select from.

*/

function FilterBar({ title, selectedStores, handleChange, items }) {
  return (
    <FormControl variant="filled">
      <InputLabel id="demo-simple-select-helper-label" size="small">
        {title}
      </InputLabel>
      <Select
        id="filterBar"
        value={selectedStores}
        multiple
        label={title}
        onChange={handleChange}
        disableUnderline
        renderValue={(selected) => selected.join(", ")}
        sx={{ height: "50px", fontSize: "small", background: "none" }}
      >
        <MenuItem disabled value="">
          {title}
        </MenuItem>
        {items.map((item) => (
          <MenuItem key={item} value={item} sx={{ fontSize: "small" }}>
            <Checkbox checked={selectedStores.indexOf(item) > -1} />
            <ListItemText primary={item} sx={{ fontSize: "small" }} />
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
}

export default FilterBar;

FilterBar.propTypes = {
  title: PropTypes.string.isRequired,
  selectedStores: PropTypes.arrayOf(PropTypes.string).isRequired,
  handleChange: PropTypes.func.isRequired,
  items: PropTypes.arrayOf(PropTypes.string).isRequired,
};
