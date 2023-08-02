import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
// @mui material components
import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import Rating from "@mui/material/Rating";

// Material Kit 2 React components
import HorizontalTeamCard from "examples/Cards/TeamCards/HorizontalTeamCard";
import MKBox from "components/MKBox";
import MKTypography from "components/MKTypography";
import listReviews from "../actions/reviewActions";
// Images
import img from "../../../assets/images/avatar.png";

/*
  Dynamic User Review Presentation component in the main page.
*/

function UserReviewPresentation() {
  const dispatch = useDispatch();
  const reviewList = useSelector((state) => state.reviewList);
  const { error, loading, reviews } = reviewList;

  useEffect(() => {
    dispatch(listReviews());
  }, [dispatch]);

  return (
    <MKBox
      component="section"
      variant="gradient"
      bgColor="dark"
      position="relative"
      py={6}
      px={{ xs: 2, lg: 0 }}
      mx={-2}
      sx={{
        width: "99.9vw",
      }}
    >
      <Container>
        <Grid container>
          <Grid item xs={12} md={8} sx={{ mb: 6 }}>
            <MKTypography variant="h3" color="white">
              Our Reviews
            </MKTypography>
            <MKTypography variant="body2" color="white" opacity={0.8}>
              We are always looking up to you.
            </MKTypography>
          </Grid>
        </Grid>
        <Grid container spacing={3}>
          {reviews &&
            reviews.map((review) => (
              <Grid item xs={12} lg={6} key={review.userCreated}>
                <MKBox mb={1}>
                  <HorizontalTeamCard
                    image={img}
                    name={review.userCreated}
                    position={{ color: "info", label: review.name }}
                    description={review.description}
                    rating={
                      <Rating
                        name="read-only"
                        precision={0.5}
                        value={parseFloat(review.rating)}
                        readOnly
                      />
                    }
                  />
                </MKBox>
              </Grid>
            ))}

          {(error || loading) && (
            <>
              <Grid item xs={12} lg={6}>
                <MKBox mb={1}>
                  <HorizontalTeamCard
                    image={img}
                    name="JohnSmith@smith.com"
                    position={{ color: "info", label: "Shop Reviewer" }}
                    description="Your website is absolutely fantastic - visually appealing, user-friendly, and filled with valuable content."
                    rating={<Rating name="read-only" precision={0.5} value={5} readOnly />}
                  />
                </MKBox>
              </Grid>
              <Grid item xs={12} lg={6}>
                <MKBox mb={1}>
                  <HorizontalTeamCard
                    image={img}
                    name="JohnSnow@snow.com"
                    position={{ color: "info", label: "Shop Reviewer" }}
                    description="Your website stands out with its sleek design, intuitive interface, and valuable information - a true delight to explore."
                    rating={<Rating name="read-only" precision={0.5} value={4.5} readOnly />}
                  />
                </MKBox>
              </Grid>
              <Grid item xs={12} lg={6}>
                <MKBox mb={{ xs: 1, lg: 0 }}>
                  <HorizontalTeamCard
                    image={img}
                    name="JohnPengo@pengo.com"
                    position={{ color: "info", label: "Shop Reviewer" }}
                    description="Bravo on creating a website that combines stunning aesthetics, seamless functionality, and rich content - a true digital masterpiece!"
                    rating={<Rating name="read-only" precision={0.5} value={4} readOnly />}
                  />
                </MKBox>
              </Grid>
              <Grid item xs={12} lg={6}>
                <MKBox mb={1}>
                  <HorizontalTeamCard
                    image={img}
                    name="Pengo@pegno.com"
                    position={{ color: "info", label: "Shop Reviewer" }}
                    description="Congratulations on an outstanding website! It's a perfect blend of style and substance, making the browsing experience enjoyable and informative."
                    rating={<Rating name="read-only" precision={0.5} value={5} readOnly />}
                  />
                </MKBox>
              </Grid>
            </>
          )}
        </Grid>
      </Container>
    </MKBox>
  );
}

export default UserReviewPresentation;
