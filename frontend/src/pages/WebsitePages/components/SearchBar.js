import { useNavigate } from "react-router-dom";
import { useState } from "react";
import PropTypes from "prop-types";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";
import SearchIcon from "@mui/icons-material/Search";

function SearchBar({ color, keyword }) {
  const navigate = useNavigate();
  const [searchValue, setSearchValue] = useState({ keyword });

  const handleInputChange = (event) => {
    const { value } = event.target;
    setSearchValue((prevState) => ({
      ...prevState,
      keyword: value,
    }));
  };

  const handleSearchButton = () => {
    navigate({
      pathname: "/search",
      search: `?keyword=${searchValue.keyword}`,
    });
  };

  return (
    <Stack spacing={1} direction="row" maxwidth="100%">
      <TextField
        id="outlined-basic"
        label="Search..."
        type="search"
        variant="outlined"
        defaultValue={searchValue.keyword}
        onChange={handleInputChange}
        sx={{
          color,
          "& label": {
            color,
            "&.Mui-focused": {
              color,
            },
          },
        }}
        inputProps={{ style: { color, width: "300px" } }}
        onKeyPress={(e) => {
          if (e.key === "Enter") {
            handleSearchButton();
          }
        }}
      />
      <Button variant="contained" onClick={handleSearchButton}>
        <SearchIcon color="white" />
      </Button>
    </Stack>
  );
}

export default SearchBar;

SearchBar.defaultProps = {
  color: "#FFF",
  keyword: "",
};

SearchBar.propTypes = {
  color: PropTypes.string,
  keyword: PropTypes.string,
  // setSearchKeyword: PropTypes.func.isRequired,
};
