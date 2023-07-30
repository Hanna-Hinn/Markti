import { Box, Pagination } from "@mui/material";
import PropTypes from "prop-types";

function PaginationComp({ totalPages, page, pageHandleChange }) {
  return (
    <Box
      justifyContent="center"
      alignItems="center"
      display="flex"
      sx={{
        margin: "20px 0px",
      }}
    >
      <Pagination count={totalPages} page={page} onChange={pageHandleChange} />
    </Box>
  );
}

export default PaginationComp;

PaginationComp.defaultProps = {
  totalPages: 10,
  page: 1,
};

PaginationComp.propTypes = {
  totalPages: PropTypes.number,
  page: PropTypes.number,
  pageHandleChange: PropTypes.func.isRequired,
};
