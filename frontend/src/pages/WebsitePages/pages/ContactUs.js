import { useState } from "react";
import axios from "axios";

// @mui material components
import Grid from "@mui/material/Grid";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import Rating from "@mui/material/Rating";
import Box from "@mui/material/Box";
import StarIcon from "@mui/icons-material/Star";
import Snackbar from "@mui/material/Snackbar";
import MuiAlert from "@mui/material/Alert";

// Material Kit 2 React components
import MKBox from "components/MKBox";
import MKInput from "components/MKInput";
import MKButton from "components/MKButton";
import MKTypography from "components/MKTypography";

// Material Kit 2 React examples
import DefaultFooter from "examples/Footers/DefaultFooter";

// Routes
import footerRoutes from "footer.routes";

//  image
import bgImage from "../../../assets/images/bg-contactUs.jpg";

const labels = {
  0.5: "Useless",
  1: "Useless+",
  1.5: "Poor",
  2: "Poor+",
  2.5: "Ok",
  3: "Ok+",
  3.5: "Good",
  4: "Good+",
  4.5: "Excellent",
  5: "Excellent+",
};

function getLabelText(value) {
  return `${value} Star${value !== 1 ? "s" : ""}, ${labels[value]}`;
}

function ContactUs() {
  const [type, setType] = useState("FeedBack");
  const [ratingValue, setRatingValue] = useState(0);
  const [hover, setHover] = useState(-1);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [email, setEmail] = useState("");
  const [error, setError] = useState({ title: true, description: true, email: true });
  const [responseCheck, setResponseCheck] = useState({ check: false, message: "error" });

  const handleChange = (event) => {
    setType(event.target.value);
  };

  const handleSubmit = () => {
    if (
      title !== "" &&
      title !== null &&
      title !== undefined &&
      description !== "" &&
      description !== null &&
      description !== undefined &&
      email !== "" &&
      email !== null &&
      email !== undefined
    ) {
      axios
        .post("http://127.0.0.1:8000/api/tickets/create", {
          name: title,
          type,
          rating: ratingValue,
          description,
          createdAt: new Date(),
          userCreated: email,
          status: "open",
        })
        .then((response) => {
          setResponseCheck({ ...responseCheck, check: true });
          if (response.status === 201) {
            setResponseCheck({ check: true, message: "success" });
          } else {
            setResponseCheck({ ...responseCheck, message: "error" });
          }
        })
        .catch(() => {
          setResponseCheck({ check: true, message: "error" });
        });
    } else {
      if (title === "" && title === null && title === undefined) {
        setError({ ...error, title: true });
      }
      if (description === "" && description === null && description === undefined) {
        setError({ ...error, description: true });
      }
      if (email === "" && email === null && email === undefined) {
        setError({ ...error, email: true });
      }
    }
  };

  const handleTitleChange = (event) => {
    if (event.target.value === "" || event.target.value === undefined) {
      setError({ ...error, title: true });
    } else {
      setError({ ...error, title: false });
      setTitle(event.target.value);
    }
  };

  const handleDescriptionChange = (event) => {
    if (event.target.value === "" || event.target.value === undefined) {
      setError({ ...error, description: true });
    } else {
      setError({ ...error, description: false });
      setDescription(event.target.value);
    }
  };

  const handleEmailChange = (event) => {
    if (event.target.value === "" || event.target.value === undefined) {
      setError({ ...error, email: true });
    } else {
      setError({ ...error, email: false });
      setEmail(event.target.value);
    }
  };

  return (
    <>
      <Grid
        container
        spacing={3}
        alignItems="center"
        sx={{
          backgroundImage: `url(${bgImage})`,
          backgroundSize: "100% 100%",
          backgroundRepeat: "no-repeat",
        }}
      >
        <Grid item xs={12} lg={6}>
          <MKBox
            display={{ xs: "none", lg: "flex" }}
            width="calc(100% - 2rem)"
            height="calc(100vh - 2rem)"
            borderRadius="lg"
            ml={2}
            mt={2}
          />
        </Grid>
        <Grid
          item
          xs={12}
          sm={10}
          md={7}
          lg={6}
          xl={4}
          ml={{ xs: "auto", lg: 6 }}
          mr={{ xs: "auto", lg: 6 }}
        >
          <MKBox
            bgColor="#FFFFFF"
            borderRadius="xl"
            shadow="lg"
            coloredShadow="dark"
            display="flex"
            flexDirection="column"
            justifyContent="center"
            mt={{ xs: 20, sm: 18, md: 20 }}
            mb={{ xs: 20, sm: 18, md: 20 }}
            mx={3}
          >
            <MKBox
              variant="gradient"
              bgColor="info"
              coloredShadow="info"
              borderRadius="lg"
              p={2}
              mx={2}
              mt={-3}
            >
              <MKTypography variant="h3" color="white">
                Contact us
              </MKTypography>
            </MKBox>
            <MKBox p={3}>
              <MKTypography variant="body2" color="text" mb={3}>
                For further questions, including partnership opportunities, please email
                hanna.hinn30@gmail.com or contact using our contact form.
              </MKTypography>
              <MKBox width="100%">
                <Grid container spacing={3}>
                  <Grid item xs={8}>
                    <FormControl fullWidth>
                      <InputLabel id="demo-simple-select-label">Type</InputLabel>
                      <Select variant="standard" value={type} label="Type" onChange={handleChange}>
                        <MenuItem value="FeedBack">FeedBack</MenuItem>
                        <MenuItem value="Suggestions">Suggestions</MenuItem>
                        <MenuItem value="Review">Review</MenuItem>
                      </Select>
                    </FormControl>
                  </Grid>

                  <Grid item xs={12} md={6}>
                    <MKInput
                      variant="standard"
                      error={error.title}
                      label="Title"
                      InputLabelProps={{ shrink: true }}
                      fullWidth
                      onChange={handleTitleChange}
                    />
                  </Grid>
                  <Grid item xs={12} md={6}>
                    <MKInput
                      type="email"
                      variant="standard"
                      label="Email"
                      InputLabelProps={{ shrink: true }}
                      fullWidth
                      error={error.email}
                      onChange={handleEmailChange}
                    />
                  </Grid>
                  <Grid item xs={12}>
                    <Rating
                      name="hover-feedback"
                      value={ratingValue}
                      precision={0.5}
                      getLabelText={getLabelText}
                      onChange={(event, newValue) => {
                        setRatingValue(newValue);
                      }}
                      onChangeActive={(event, newHover) => {
                        setHover(newHover);
                      }}
                      emptyIcon={<StarIcon style={{ opacity: 0.55 }} fontSize="inherit" />}
                    />
                    {ratingValue !== null && (
                      <Box sx={{ ml: 2 }}>{labels[hover !== -1 ? hover : ratingValue]}</Box>
                    )}
                  </Grid>
                  <Grid item xs={12}>
                    <MKInput
                      variant="standard"
                      label="What can we help you?"
                      placeholder="Describe your problem in at least 250 characters"
                      InputLabelProps={{ shrink: true }}
                      error={error.description}
                      onChange={handleDescriptionChange}
                      multiline
                      fullWidth
                      rows={6}
                    />
                  </Grid>
                </Grid>
                <Grid container item justifyContent="center" xs={12} mt={5} mb={2}>
                  <MKButton type="submit" variant="gradient" color="info" onClick={handleSubmit}>
                    Send Message
                  </MKButton>
                </Grid>
              </MKBox>
            </MKBox>
          </MKBox>
        </Grid>
      </Grid>
      <Snackbar open={responseCheck.check} autoHideDuration={5000}>
        <MuiAlert
          open={responseCheck.check}
          severity={responseCheck.message}
          sx={{ width: "100%" }}
        >
          {responseCheck.message === "success"
            ? "Operation Success, We will contact as soon as possible!"
            : "Operation Failed, Please Try Again"}
        </MuiAlert>
      </Snackbar>

      <MKBox pt={6} px={1} mt={6}>
        <DefaultFooter content={footerRoutes} />
      </MKBox>
    </>
  );
}

export default ContactUs;
