import PropTypes from "prop-types";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";

function SortSelectBar({ title, value, handleChange, items }) {
  return (
    <FormControl variant="filled" sx={{ marginTop: 5, width: "15%" }}>
      <InputLabel id="demo-simple-select-helper-label" size="small">
        {title}
      </InputLabel>
      <Select
        id="sortSelectBar"
        value={value}
        label={title}
        onChange={handleChange}
        disableUnderline
        sx={{ height: "50px", fontSize: "small", background: "none" }}
      >
        <MenuItem value="">{title}</MenuItem>
        {items.map((item) => (
          <MenuItem value={item}>{item}</MenuItem>
        ))}
      </Select>
    </FormControl>
  );
}

export default SortSelectBar;

SortSelectBar.propTypes = {
  title: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
  handleChange: PropTypes.func.isRequired,
  items: PropTypes.arrayOf(PropTypes.string).isRequired,
};
