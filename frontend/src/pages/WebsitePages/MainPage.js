import footerRoutes from "../../footer.routes";
import MKBox from "../../components/MKBox";
import DefaultFooter from "../../examples/Footers/DefaultFooter";
import Header from "./components/header";
import FeaturesOne from "./components/Features";
import UserReviewPresentation from "./components/UserReviewPresentation";

function MainPage() {
  return (
    <>
      <Header />
      <FeaturesOne />
      <UserReviewPresentation />
      <MKBox pt={6} px={1} mt={6}>
        <DefaultFooter content={footerRoutes} />
      </MKBox>
    </>
  );
}

export default MainPage;
