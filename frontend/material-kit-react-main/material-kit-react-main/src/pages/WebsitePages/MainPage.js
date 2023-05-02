import footerRoutes from "../../footer.routes";
import MKBox from "../../components/MKBox";
import DefaultFooter from "../../examples/Footers/DefaultFooter";
import Header from "./header";

function MainPage() {
  return (
    <>
      <Header />
      <MKBox pt={6} px={1} mt={6}>
        <DefaultFooter content={footerRoutes} />
      </MKBox>
    </>
  );
}

export default MainPage;
