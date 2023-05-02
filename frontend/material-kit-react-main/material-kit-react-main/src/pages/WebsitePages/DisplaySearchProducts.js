import { useState, useEffect } from "react";
import axios from "axios";
import Stack from "@mui/material/Stack";
import footerRoutes from "../../footer.routes";
import MKBox from "../../components/MKBox";
import DefaultFooter from "../../examples/Footers/DefaultFooter";
import Product from "./components/Product";
import NavHead from "./components/Navhead";
// import proImg from "../../assets/images/products/product2.jpg";
import AdCard from "./components/AdCard";
import SortSelectBar from "./components/sortSelectBar";
// import FilterAside from "./components/filterAside";

function DisplaySearchProducts() {
  // const [keyword, setKeyword] = useState();
  const [products, setProducts] = useState([]);
  const [sortedProducts, setSortedProducts] = useState([...products]);
  const [sort, setSort] = useState("");

  // const products = [
  //   {
  //     product_id: 1,
  //     product_title: "Product1",
  //     product_category: "Category1",
  //     product_image: proImg,
  //     product_url: "https:www.google.com",
  //     product_price: "30",
  //     product_store: "amazon",
  //     product_store_image:
  //       "https://cached.imagescaler.hbpl.co.uk/resize/scaleWidth/952/cached.offlinehbpl.hbpl.co.uk/news/NST/Amazon-logo-meaning.jpg",
  //     product_rating: 4,
  //   },
  //   {
  //     product_id: 2,
  //     product_title: "Product2",
  //     product_category: "Category2",
  //     product_image: proImg,
  //     product_url: "https:www.google.com",
  //     product_price: "30",
  //     product_store: "ebay",
  //     product_store_image:
  //       "https://cached.imagescaler.hbpl.co.uk/resize/scaleWidth/952/cached.offlinehbpl.hbpl.co.uk/news/NST/Amazon-logo-meaning.jpg",
  //     product_rating: 3,
  //   },
  //   {
  //     product_id: 3,
  //     product_title: "Product3",
  //     product_category: "Category3",
  //     product_image: proImg,
  //     product_url: "https:www.google.com",
  //     product_price: "30",
  //     product_store: "amazon",
  //     product_store_image:
  //       "https://cached.imagescaler.hbpl.co.uk/resize/scaleWidth/952/cached.offlinehbpl.hbpl.co.uk/news/NST/Amazon-logo-meaning.jpg",
  //     product_rating: 2,
  //   },
  // ];

  useEffect(() => {
    const searchParams = new URLSearchParams(window.location.search);
    // Update the component state with the name
    const keyword = searchParams.get("keyword" || "");

    async function fetchProducts() {
      const { data } = await axios.get(`http://127.0.0.1:8000/api/start?keyword=${keyword}`);
      setProducts(data);
    }
    fetchProducts();
  }, []);

  function sortProducts(unSortedProducts, sortOption) {
    const result = [...unSortedProducts];
    switch (sortOption) {
      case "Price ⬇-⬆":
        result.sort((a, b) => a.product_price - b.product_price);
        break;
      case "Price ⬆-⬇":
        result.sort((a, b) => b.product_price - a.product_price);
        break;
      case "Alphabetical A-Z":
        result.sort((a, b) => a.product_title.localeCompare(b.product_title));
        break;
      case "Alphabetical Z-A":
        result.sort((a, b) => b.product_title.localeCompare(a.product_title));
        break;
      // case "Rating":
      //   sortedProducts.sort((a, b) => b.product_rating - a.product_rating);
      //   break;
      default:
        result.sort((a, b) => a.product_price - b.product_price);
        break;
    }

    return result;
  }

  useEffect(() => {
    const sortResult = sortProducts(products, sort);
    setSortedProducts(sortResult);
  }, [products, sort]);

  const handleChange = (event) => {
    setSort(event.target.value);
    // const sortedProducts = sortProducts(products, sort);
    // setProducts(sortedProducts);
  };

  return (
    <>
      <NavHead position="relative" includeSearchBar />
      <MKBox display="flex" sx={{ margin: 1, minHeight: "100vh" }}>
        <AdCard />
        <Stack spacing={2} sx={{ flexBasis: "50%" }}>
          <SortSelectBar
            title="Sort"
            value={sort}
            handleChange={handleChange}
            items={["Price ⬆-⬇", "Price ⬇-⬆", "Alphabetical A-Z", "Alphabetical Z-A"]}
          />
          {sortedProducts.map((product) => (
            <Product
              key={product.product_id}
              title={product.product_title}
              category={product.product_category}
              image={product.product_image}
              url={product.product_url}
              price={product.product_price}
              rating={`${product.product_rating}`}
              store={product.product_store}
              storeImg={product.product_store_image}
            />
          ))}
        </Stack>
        <AdCard />
      </MKBox>
      <MKBox pt={6} px={1} mt={6}>
        <DefaultFooter content={footerRoutes} />
      </MKBox>
    </>
  );
}

export default DisplaySearchProducts;
