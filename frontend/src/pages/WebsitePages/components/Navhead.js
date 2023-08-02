import { useState } from "react";
import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import Link from "@mui/material/Link";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import InfoIcon from "@mui/icons-material/Info";
import HomeIcon from "@mui/icons-material/Home";
import ContactPageIcon from "@mui/icons-material/ContactPage";
import PropTypes from "prop-types";
import MKBox from "../../../components/MKBox";
import MKButton from "../../../components/MKButton";
import MKTypography from "../../../components/MKTypography";
import SearchBar from "./SearchBar";

/*
  Header Navigation Component

  props: 
    1.) color (string): changes the text color based on the background colors.
    2.) position (string): changes the position type either absolute or relative.
    3.) includeSearchBar (bool): display or not display the search bar in the navigation
    4.) searchValue (string) : Fills the search bar with the searched value if exists.
*/

function NavHead({ color, position, includeSearchBar, searchValue }) {
  const [openNav, setOpenNav] = useState(false);

  const navOnClickHandler = () => {
    setOpenNav(!openNav);
  };

  return (
    <MKBox
      component="nav"
      position={position}
      top="0.5rem"
      width="100%"
      marginBottom="10px"
      sx={{
        paddingLeft: "0px",
        right: "4px",
      }}
    >
      <Container>
        <Grid container flexDirection="row" alignItems="space-between">
          <MKTypography
            component={Link}
            href="#/"
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
            onClick={navOnClickHandler}
          >
            <MKBox component="li" color={color} className="fas fa-bars" />
            {openNav && (
              <List sx={{ color: "white" }}>
                <ListItem disablePadding>
                  <ListItemButton component="a" href="#/home">
                    <ListItemIcon>
                      <HomeIcon />
                    </ListItemIcon>
                    <ListItemText secondary="Home" />
                  </ListItemButton>
                </ListItem>
                <ListItem disablePadding>
                  <ListItemButton component="a" href="#/about-us">
                    <ListItemIcon>
                      <InfoIcon />
                    </ListItemIcon>
                    <ListItemText secondary="About Us" />
                  </ListItemButton>
                </ListItem>
                <ListItem disablePadding>
                  <ListItemButton component="a" href="#/contact-us">
                    <ListItemIcon>
                      <ContactPageIcon />
                    </ListItemIcon>
                    <ListItemText secondary="Contact Us" />
                  </ListItemButton>
                </ListItem>
              </List>
            )}
          </MKButton>

          <MKBox
            component="ul"
            display={{ xs: "none", lg: "flex" }}
            p={0}
            my={0}
            mx="auto"
            sx={{ listStyle: "none" }}
          >
            {includeSearchBar && <SearchBar color="black" keyword={searchValue} />}
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
                href="#/home"
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
                href="#/about-us"
                variant="button"
                color={color}
                fontWeight="regular"
                p={1}
              >
                About Us
              </MKTypography>
            </MKBox>
            <MKBox component="li">
              <MKTypography
                component={Link}
                href="#/contact-us"
                variant="button"
                color={color}
                fontWeight="regular"
                p={1}
              >
                Contact Us
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
  searchValue: "",
};

NavHead.propTypes = {
  color: PropTypes.string,
  position: PropTypes.string,
  searchValue: PropTypes.string,
  includeSearchBar: PropTypes.bool,
};

export default NavHead;
