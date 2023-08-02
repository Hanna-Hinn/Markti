import { Box, Pagination } from "@mui/material";
import PropTypes from "prop-types";

/*
    **Since we can not achieve a fast pagination in the back we have decided to make it from the front.

    Pagination component

    params: 1.) totalPages : the total amount of pages
            2.) page : Which page the user at
            3.) pageHandleChange : Event listener function that changes the value of the page state when the user changes the page. 

 */

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
