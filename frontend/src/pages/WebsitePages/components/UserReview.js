import { useState } from "react";
import axios from "axios";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import CloseIcon from "@mui/icons-material/Close";
import Rating from "@mui/material/Rating";
import Snackbar from "@mui/material/Snackbar";
import MuiAlert from "@mui/material/Alert";

function getCSRFToken() {
  const csrfCookie = document.cookie.match(/(^|;) ?csrftoken=([^;]*)(;|$)/);
  return csrfCookie ? csrfCookie[2] : null;
}

function UserReview() {
  const [open, setOpen] = useState(true);
  const [ratingValue, setRatingValue] = useState(0);
  const [emailValue, setEmailValue] = useState("");
  const [descriptionValue, setDescriptionValue] = useState("");
  const [responseCheck, setResponseCheck] = useState({ check: false, message: "error" });
  const csrfToken = getCSRFToken();

  const ratingOnChangeHandle = (event, newValue) => {
    setRatingValue(newValue);
  };

  const emailOnChangeHandle = (event) => {
    setEmailValue(event.target.value);
  };

  const descriptionOnChangeHandle = (event) => {
    setDescriptionValue(event.target.value);
  };

  const close = () => {
    setOpen(false);
  };

  const submitOnClick = () => {
    if (
      emailValue !== "" &&
      emailValue !== null &&
      descriptionValue !== "" &&
      descriptionValue !== null
    ) {
      axios
        .post(
          "https://marketi-ps-caab34e05b6a.herokuapp.com/api/tickets/create",
          {
            name: "Reviewer",
            type: "Review",
            rating: ratingValue,
            description: descriptionValue,
            createdAt: new Date(),
            userCreated: emailValue,
            status: "open",
          },
          {
            headers: {
              "X-CSRFToken": csrfToken,
            },
          }
        )
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
    }

    close();
  };

  return (
    <>
      {open && (
        <Box
          sx={{
            p: 2,
            width: "100vw",
            border: "1px dashed grey",
            display: "flex",
            flexWrap: "warp",
            flexFlow: "wrap",
            alignItems: "baseline",
            alignContent: "space-between",
            gap: "30px",
          }}
        >
          <Typography variant="overline" gutterBottom>
            Enjoying your experience? Help us out by sharing your thoughts and rating our website!
          </Typography>
          <Rating
            name="controlled-rating"
            value={ratingValue}
            onChange={ratingOnChangeHandle}
            precision={0.5}
          />
          <TextField
            required
            id="email-outlined-required"
            label="Enter your email"
            onChange={emailOnChangeHandle}
          />
          <TextField
            required
            id="description-outlined-required"
            label="Enter a description"
            onChange={descriptionOnChangeHandle}
          />
          <Button variant="contained" onClick={submitOnClick} sx={{ color: "#FFF" }}>
            Rate
          </Button>
          <Button variant="outlined" sx={{ color: "#000" }} endIcon={<CloseIcon />} onClick={close}>
            Close
          </Button>
          <Snackbar open={responseCheck.check} autoHideDuration={5000}>
            <MuiAlert
              open={responseCheck.check}
              severity={responseCheck.message}
              sx={{ width: "100%" }}
            >
              {responseCheck.message === "success"
                ? "Operation Success, Thank you for Rating Us!"
                : "Operation Failed, Please Try Again"}
            </MuiAlert>
          </Snackbar>
        </Box>
      )}
    </>
  );
}

export default UserReview;
