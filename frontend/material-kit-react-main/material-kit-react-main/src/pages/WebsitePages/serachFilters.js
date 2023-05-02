import Chip from "@mui/material/Chip";
import Stack from "@mui/material/Stack";
import PropTypes from "prop-types";

function SearchFilter({ name }) {
  return (
    <Stack direction="row" spacing={1}>
      <Chip label={name} variant="outlined" />
    </Stack>
  );
}

SearchFilter.propTypes = {
  name: PropTypes.string.isRequired,
};

export default SearchFilter;
