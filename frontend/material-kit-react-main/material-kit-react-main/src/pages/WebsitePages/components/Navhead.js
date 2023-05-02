import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import Link from "@mui/material/Link";
import PropTypes from "prop-types";
import MKBox from "../../../components/MKBox";
import MKButton from "../../../components/MKButton";
import MKTypography from "../../../components/MKTypography";
import SearchBar from "./SearchBar";

function NavHead({ color, position, includeSearchBar }) {
  return (
    <MKBox
      component="nav"
      position={position}
      top="0.5rem"
      width="100%"
      marginBottom="10px"
      // sx={{ marginBottom: "10px" }}
    >
      <Container>
        <Grid container flexDirection="row" alignItems="center">
          <MKTypography
            component={Link}
            href="/"
            variant="button"
            color={color}
            fontWeight="regular"
            py={0.8125}
            mr={2}
          >
            Marketi
          </MKTypography>
          <MKButton
            variant="outlined"
            color={color}
            sx={{ display: { xs: "block", lg: "none" }, ml: "auto" }}
          >
            <MKBox component="i" color={color} className="fas fa-bars" />
          </MKButton>
          {includeSearchBar && <SearchBar color="black" />}
          <MKBox
            component="ul"
            display={{ xs: "none", lg: "flex" }}
            p={0}
            my={0}
            mx="auto"
            sx={{ listStyle: "none" }}
          >
            <MKBox component="li">
              <MKTypography
                component={Link}
                href="/"
                variant="button"
                color={color}
                fontWeight="regular"
                p={1}
                // onClick={(e) => e.preventDefault()}
              >
                Home
              </MKTypography>
            </MKBox>
            <MKBox component="li">
              <MKTypography
                component={Link}
                href="#"
                variant="button"
                color={color}
                fontWeight="regular"
                p={1}
                onClick={(e) => e.preventDefault()}
              >
                About Us
              </MKTypography>
            </MKBox>
            <MKBox component="li">
              <MKTypography
                component={Link}
                href="#"
                variant="button"
                color={color}
                fontWeight="regular"
                p={1}
                onClick={(e) => e.preventDefault()}
              >
                Contact Us
              </MKTypography>
            </MKBox>
          </MKBox>
          <MKBox
            component="ul"
            display={{ xs: "none", lg: "flex" }}
            p={0}
            m={0}
            sx={{ listStyle: "none" }}
          >
            <MKBox component="li">
              <MKTypography
                component={Link}
                href="#"
                variant="button"
                p={1}
                onClick={(e) => e.preventDefault()}
              >
                <MKBox component="i" color={color} className="fab fa-twitter" />
              </MKTypography>
            </MKBox>
            <MKBox component="li">
              <MKTypography
                component={Link}
                href="#"
                variant="button"
                p={1}
                onClick={(e) => e.preventDefault()}
              >
                <MKBox component="i" color={color} className="fab fa-facebook" />
              </MKTypography>
            </MKBox>
            <MKBox component="li">
              <MKTypography
                component={Link}
                href="#"
                variant="button"
                p={1}
                onClick={(e) => e.preventDefault()}
              >
                <MKBox component="i" color={color} className="fab fa-instagram" />
              </MKTypography>
            </MKBox>
          </MKBox>
        </Grid>
      </Container>
    </MKBox>
  );
}

NavHead.defaultProps = {
  color: "dark",
  position: "absolute",
  includeSearchBar: false,
};

NavHead.propTypes = {
  color: PropTypes.string,
  position: PropTypes.string,
  includeSearchBar: PropTypes.bool,
};

export default NavHead;
