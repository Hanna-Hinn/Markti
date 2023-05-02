import Card from "@mui/material/Card";
import PropTypes from "prop-types";
import CardContent from "@mui/material/CardContent";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import { CardActionArea } from "@mui/material";
import Rating from "@mui/material/Rating";
import Grid from "@mui/material/Grid";

function Product({ title, category, image, url, price, rating, store, storeImg }) {
  return (
    <Card
      sx={{
        maxWidth: "100%",
        display: "flex",
        marginTop: 5,
        minHeight: "200px",
      }}
    >
      <CardActionArea href={url}>
        <CardContent>
          <Grid container spacing={3}>
            <Grid item xs>
              <Box
                component="img"
                alt={title}
                src={image}
                sx={{ height: "100px", width: "100px", backgroundSize: "cover" }}
              />
            </Grid>
            <Grid item xs={6}>
              <Typography gutterBottom variant="h5">
                {title}
              </Typography>
              <Typography gutterBottom variant="body2" color="text.secondary">
                {category}
              </Typography>
              <Typography variant="h4">{price}$</Typography>
              <Rating name="Rating" value={rating} readOnly />
            </Grid>
            <Grid item xs>
              {/* <Box
                display="flex"
                justifyContent="center"
                alignItems="center"
                sx={{ height: "100%", width: "100%" }}
              > */}
              <Box
                component="img"
                alt={store}
                src={storeImg}
                sx={{ backgroundSize: "cover", width: "100px", height: "100px" }}
              />
              {/* </Box> */}
            </Grid>
          </Grid>
        </CardContent>
      </CardActionArea>
    </Card>
  );
}

Product.propTypes = {
  title: PropTypes.string.isRequired,
  category: PropTypes.string.isRequired,
  image: PropTypes.string.isRequired,
  url: PropTypes.string.isRequired,
  price: PropTypes.string.isRequired,
  rating: PropTypes.number.isRequired,
  store: PropTypes.string.isRequired,
  storeImg: PropTypes.string.isRequired,
};

export default Product;
