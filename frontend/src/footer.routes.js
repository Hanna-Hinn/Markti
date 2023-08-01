// @mui icons
import FacebookIcon from "@mui/icons-material/Facebook";
import TwitterIcon from "@mui/icons-material/Twitter";
import LinkedInIcon from "@mui/icons-material/LinkedIn";
import InstagramIcon from "@mui/icons-material/Instagram";

// Material Kit 2 React components
import MKTypography from "./components/MKTypography";

// Images
import logoCT from "./assets/images/avatar.png";

const date = new Date().getFullYear();

export default {
  brand: {
    name: "Marketi",
    image: logoCT,
    route: "/home",
  },
  socials: [
    {
      icon: <FacebookIcon />,
      link: "https://www.facebook.com",
    },
    {
      icon: <TwitterIcon />,
      link: "https://twitter.com/Marketi315590",
    },
    {
      icon: <LinkedInIcon />,
      link: "https://linkedin.com",
    },
    {
      icon: <InstagramIcon />,
      link: "https://www.instagram.com",
    },
  ],
  menus: [
    {
      name: "company",
      items: [
        { name: "home", href: "#/home" },
        { name: "about us", href: "#/about-us" },
      ],
    },
    {
      name: "resources",
      items: [{ name: "coming-soon", href: "#/docs" }],
    },
    {
      name: "help & support",
      items: [
        { name: "Contact Us", href: "#/contact-us" },
        { name: "Suggestions", href: "#/contact-us" },
      ],
    },
    {
      name: "legal",
      items: [
        { name: "terms & conditions", href: "#/terms-conditions" },
        { name: "privacy policy", href: "#/privacy-policy" },
      ],
    },
  ],
  copyright: (
    <MKTypography variant="button" fontWeight="regular">
      All rights reserved. Copyright &copy; {date}{" "}
      <MKTypography
        component="a"
        target="_blank"
        rel="noreferrer"
        variant="button"
        fontWeight="regular"
      >
        Marketi
      </MKTypography>
      .
    </MKTypography>
  ),
};
