import * as React from "react";
import PropTypes from "prop-types";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import OfflinePinIcon from "@mui/icons-material/OfflinePin";
import Rating from "@mui/material/Rating";
import Typography from "@mui/material/Typography";
import Tooltip from "@mui/material/Tooltip";
import Box from "@mui/material/Box";
import "./ProductTable.css";
import img from "../../../assets/images/noResults.png";

export default function ProductTable({ rows }) {
  if (rows.length > 0) {
    return (
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableBody>
            {rows.map((row) => (
              <TableRow
                key={row.product_id}
                sx={{
                  "&:last-child td, &:last-child th": { border: 0 },
                }}
              >
                <TableCell component="th" scope="row">
                  <img
                    className="productImage"
                    src={`${row.product_image}?w=164&h=164&fit=crop&auto=format`}
                    srcSet={`${row.product_image}?w=164&h=164&fit=crop&auto=format&dpr=2 2x`}
                    alt={row.title}
                    loading="lazy"
                  />
                </TableCell>
                <TableCell align="right">
                  <Typography gutterBottom variant="h6">
                    {row.product_title}
                  </Typography>
                </TableCell>
                <TableCell align="right">
                  <Typography gutterBottom variant="body2" color="text.secondary">
                    {row.product_category}
                  </Typography>
                </TableCell>
                <TableCell align="right">
                  <Typography variant="h6">{row.product_price}</Typography>
                </TableCell>
                <TableCell align="right">
                  {row.product_rating && (
                    <Rating
                      name="Rating"
                      value={
                        Number(row.product_rating) <= 5
                          ? Number(row.product_rating)
                          : Number(row.product_rating) / 20
                      }
                      readOnly
                    />
                  )}
                  {(row.product_trusted === "true" || row.product_trusted === "Trusted") && (
                    <>
                      <Typography variant="h6">Trusted</Typography>
                      <Tooltip title="Trusted">
                        <OfflinePinIcon color="success" />
                      </Tooltip>
                    </>
                  )}
                  {(row.product_trusted === "false" || row.product_trusted === "NotTrusted") && (
                    <>
                      <Typography variant="h6">Not Trusted</Typography>
                      <Tooltip title="Not Trusted">
                        <OfflinePinIcon sx={{ color: "#FF0000" }} />
                      </Tooltip>
                    </>
                  )}
                </TableCell>
                <TableCell align="right">
                  <a href={row.product_url} target="_blank" rel="noreferrer noopener">
                    <img
                      src={`${row.product_store_image}?w=164&h=164&fit=crop&auto=format`}
                      srcSet={`${row.product_store_image}?w=164&h=164&fit=crop&auto=format&dpr=2 2x`}
                      width="100"
                      alt={row.store}
                      loading="lazy"
                    />
                  </a>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    );
  }
  return (
    <>
      <Typography variant="h1" gutterBottom>
        No Results Was found
      </Typography>

      <Typography variant="h6" gutterBottom>
        Try checking your spelling or use more general terms
      </Typography>
      <Box
        component="img"
        sx={{
          height: 500,
          width: 500,
          maxHeight: { xs: 300, md: 300 },
          maxWidth: { xs: 500, md: 500 },
        }}
        alt="No result Found"
        src={img}
      />
    </>
  );
}

ProductTable.propTypes = {
  rows: PropTypes.arrayOf(PropTypes.object).isRequired,
};
