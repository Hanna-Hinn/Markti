// @mui material components
// import PropTypes from "prop-types";
import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";

import bgImage from "../../../assets/images/bg-landing-two.jpeg";

// Material Kit 2 React components
import MKBox from "../../../components/MKBox";
import MKTypography from "../../../components/MKTypography";
import NavHead from "./Navhead";
import SearchBar from "./SearchBar";

// Images

function Header() {
  return (
    <MKBox component="header" position="relative" sx={{ padding: "0px" }}>
      <NavHead color="white" position="absolute" />
      <MKBox
        display="flex"
        alignItems="center"
        minHeight="100vh"
        sx={{
          backgroundImage: ({ palette: { gradients }, functions: { linearGradient, rgba } }) =>
            `${linearGradient(
              rgba(gradients.dark.main, 0.5),
              rgba(gradients.dark.state, 0.5)
            )}, url(${bgImage})`,
          backgroundSize: "cover",
          backgroundPosition: "center",
        }}
      >
        <Container>
          <Grid container item xs={12} md={7} lg={6} flexDirection="column" justifyContent="center">
            <MKTypography
              variant="h1"
              color="light"
              mb={3}
              sx={({ breakpoints, typography: { size } }) => ({
                [breakpoints.down("md")]: {
                  fontSize: size["3xl"],
                },
              })}
            >
              Marketi
            </MKTypography>
            <MKTypography variant="body1" color="white" opacity={0.8} pr={6} mr={6}>
              The Only Store You Will Need
            </MKTypography>
            <SearchBar />
          </Grid>
        </Container>
      </MKBox>
    </MKBox>
  );
}

export default Header;

// Header.propTypes = {
//   setSearchWord: PropTypes.func.isRequired,
// };
