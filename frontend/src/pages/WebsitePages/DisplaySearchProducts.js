import PropTypes from "prop-types";
import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useLocation } from "react-router-dom";
import Stack from "@mui/material/Stack";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Alert from "@mui/material/Alert";
import AlertTitle from "@mui/material/AlertTitle";
import Snackbar from "@mui/material/Snackbar";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import LinearProgress from "@mui/material/LinearProgress";

import footerRoutes from "../../footer.routes";
import MKBox from "../../components/MKBox";
import DefaultFooter from "../../examples/Footers/DefaultFooter";
import NavHead from "./components/Navhead";
import AdCard from "./components/AdCard";
// import SortSelectBar from "./components/sortSelectBar";
import PaginationComp from "./components/PaginationComp";
import ProductTable from "./components/ProductTable";
import FilterButton from "./components/FilterButton";
import listProducts from "./actions/productActions";
import SkeletonTable from "./components/skeletonTable";
import UserReview from "./components/UserReview";
import ApiErrorMessage from "./components/ApiErrorMessage";

// import filterList from "./actions/filterActions";

function DisplaySearchProducts({ searchWord }) {
  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const keyword = searchParams.get("keyword" || "");
  const dispatch = useDispatch();
  const productList = useSelector((state) => state.productList);
  // const filteredList = useSelector((state) => state.filteredProducts);
  const { error, loading, products, maxPrice, apiEmpty } = productList;
  // const { filteredProducts } = filteredList;
  const [sort, setSort] = useState({ type: "price", asceOrDesc: "True" });
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(10);
  const [currentProducts, setCurrentProducts] = useState([]);
  const [postsPerPage] = useState(20);
  const indexOfLastPost = currentPage * postsPerPage;
  const indexOfFirstPost = indexOfLastPost - postsPerPage;
  const [filterState, setFilterState] = useState({
    rating: [],
    stores: [],
    price: [0, maxPrice],
  });
  const [filteredData, setFilteredData] = useState([]);
  const items = [
    "Price ⬆-⬇",
    "Price ⬇-⬆",
    "Alphabetical A-Z",
    "Alphabetical Z-A",
    "Rating ⬇-⬆",
    "Rating ⬆-⬇",
  ];
  const [displaySort, setDisplaySort] = useState("Price ⬇-⬆");

  const pageHandleChange = (event, value) => {
    setCurrentPage(value);
    window.scrollTo(0, 0);
  };

  const applyFilters = () => {
    setCurrentProducts([]);
    if (filterState.rating.length > 0 && filterState.stores.length > 0) {
      const result = products.filter(
        (product) =>
          filterState.rating.some((value) => value === product.product_rating) &&
          filterState.stores.some((value) => value === product.product_store) &&
          product.product_price >= filterState.price[0] &&
          product.product_price <= filterState.price[1]
      );
      return result;
    }
    if (filterState.rating.length === 0 && filterState.stores.length >= 1) {
      const result = products.filter(
        (product) =>
          filterState.stores.some((value) => value === product.product_store) &&
          product.product_price >= filterState.price[0] &&
          product.product_price <= filterState.price[1]
      );
      return result;
    }
    const result = products;
    return result;
  };

  useEffect(() => {
    setFilteredData([]);
    setCurrentProducts([]);
    dispatch(listProducts(keyword, sort));
    setFilteredData(products);
  }, [dispatch, sort, keyword]);

  useEffect(() => {
    setFilteredData([]);
    setFilteredData(applyFilters());
  }, [filterState]);

  useEffect(() => {
    if (products && products.length > 0) {
      setFilteredData([]);
      setFilteredData(products);
    }
  }, [products]);

  useEffect(() => {
    if (filteredData && filteredData.length > 0) {
      setTotalPages(Math.round(filteredData.length / postsPerPage));
      setCurrentProducts([]);
      setCurrentProducts(filteredData.slice(indexOfFirstPost, indexOfLastPost));
    }
  }, [filteredData]);

  useEffect(() => {
    setCurrentProducts([]);
    setCurrentProducts(filteredData.slice(indexOfFirstPost, indexOfLastPost));
  }, [currentPage, filteredData]);

  const handleChange = (event) => {
    switch (event.target.value) {
      case "Price ⬇-⬆":
        setSort({ type: "price", asceOrDesc: "True" });
        break;
      case "Price ⬆-⬇":
        setSort({ type: "price", asceOrDesc: "False" });
        break;
      case "Alphabetical A-Z":
        setSort({ type: "alphabit", asceOrDesc: "True" });
        break;
      case "Alphabetical Z-A":
        setSort({ type: "alphabit", asceOrDesc: "False" });
        break;
      case "Rating ⬇-⬆":
        setSort({ type: "rating", asceOrDesc: "True" });
        break;
      case "Rating ⬆-⬇":
        setSort({ type: "rating", asceOrDesc: "False" });
        break;
      default:
        setSort({ type: "price", asceOrDesc: "True" });
        break;
    }
    setDisplaySort(event.target.value);
  };

  return (
    <>
      <UserReview />
      <NavHead position="relative" includeSearchBar searchValue={searchWord} />
      <MKBox
        display="flex"
        sx={{ margin: 1, minHeight: "100vh", flexWrap: "wrap", justifyContent: "center" }}
      >
        <Stack spacing={1} sx={{ flexBasis: "70%" }}>
          <Container
            component="span"
            sx={{ display: "flex", flexWrap: "wrap", alignItems: "baseline" }}
          >
            {!loading && (
              <>
                {/* <SortSelectBar
                  title="Sort"
                  value={sort.type}
                  handleChange={handleChange}
                  items={[
                    "Price ⬆-⬇",
                    "Price ⬇-⬆",
                    "Alphabetical A-Z",
                    "Alphabetical Z-A",
                    "Rating ⬇-⬆",
                    "Rating ⬆-⬇",
                  ]}
                /> */}

                <FormControl variant="filled" sx={{ marginTop: 5, width: "15%" }}>
                  <InputLabel id="demo-simple-select-helper-label" size="small">
                    Sort
                  </InputLabel>
                  <Select
                    id="sortSelectBar"
                    // label={title}
                    value={displaySort}
                    onChange={handleChange}
                    disableUnderline
                    sx={{ height: "50px", fontSize: "small", background: "none" }}
                  >
                    {items.map((item) => (
                      <MenuItem key={item} value={item}>
                        {item}
                      </MenuItem>
                    ))}
                  </Select>
                </FormControl>

                <FilterButton
                  filterState={filterState}
                  setFilterState={setFilterState}
                  // minMax={[0, maxPrice]}
                  minPriceValue={0}
                  maxPriceValue={maxPrice && maxPrice}
                  applyFilters={applyFilters}
                />
                {apiEmpty && <ApiErrorMessage emptyApis={apiEmpty} />}
              </>
            )}
          </Container>
          {error && (
            <Box sx={{ maxWidth: "100%", minHeight: "20%" }}>
              <Alert severity="error">
                <AlertTitle>Error</AlertTitle>
                <strong>{error}</strong>
              </Alert>
            </Box>
          )}
          {loading && <SkeletonTable sx={{ marginTop: "5px" }} />}

          {!error && !loading && <ProductTable rows={currentProducts} />}
          {/* {!error && !loading && !filteredProducts && <ProductTable rows={products} />} */}
        </Stack>

        <AdCard />
      </MKBox>
      <PaginationComp
        totalPages={totalPages}
        page={currentPage}
        pageHandleChange={pageHandleChange}
      />
      <MKBox pt={6} px={1} mt={6}>
        <DefaultFooter content={footerRoutes} />
      </MKBox>
      <Snackbar open={loading}>
        <Box sx={{ width: "100%" }}>
          <Alert severity="info">Please Wait While We Fetch the Data!</Alert>
          <LinearProgress color="info" sx={{ overflow: "hidden" }} />
        </Box>
      </Snackbar>
    </>
  );
}

export default DisplaySearchProducts;

DisplaySearchProducts.defaultProps = {
  searchWord: "",
};

DisplaySearchProducts.propTypes = {
  searchWord: PropTypes.string,
};
