import { useState } from "react";
import { Provider } from "react-redux";

// react-router components
import { HashRouter as Router, Routes, Route } from "react-router-dom";

// @mui material components
import { ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";

import PrivacyPolicy from "pages/WebsitePages/pages/PrivacyPolicy";
import TermsAndConditions from "pages/WebsitePages/pages/TermsAndConditions";
import AboutUs from "pages/WebsitePages/pages/AboutUs";
import MainPage from "./pages/WebsitePages/MainPage";

// import routes from "./routes";
import ContactUs from "./pages/WebsitePages/pages/ContactUs";
import DisplaySearchProducts from "./pages/WebsitePages/DisplaySearchProducts";
import NotFound from "./pages/WebsitePages/pages/NotFound";

import theme from "./assets/theme";

import store from "./pages/WebsitePages/Redux/store";

export default function App() {
  const [searchWord, setSearchWord] = useState();

  return (
    <Router>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <Routes>
          <Route
            path="/"
            element={
              <Provider store={store}>
                <MainPage setSearchWord={setSearchWord} />
              </Provider>
            }
          />
          <Route
            path="/search"
            element={
              <Provider store={store}>
                <DisplaySearchProducts searchWord={searchWord} />
              </Provider>
            }
          />
          <Route path="/contact-us" element={<ContactUs />} />
          <Route path="/about-us" element={<AboutUs />} />
          <Route path="/terms-conditions" element={<TermsAndConditions />} />
          <Route path="/privacy-policy" element={<PrivacyPolicy />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </ThemeProvider>
    </Router>
  );
}
