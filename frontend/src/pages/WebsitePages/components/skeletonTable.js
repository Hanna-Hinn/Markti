import Stack from "@mui/material/Stack";
import Skeleton from "@mui/material/Skeleton";

function SkeletonTable() {
  return (
    <Stack spacing={1} sx={{ width: "100%" }}>
      <Skeleton variant="rectangular" sx={{ maxWidth: "100%", minHeight: "50%" }} />
      <Skeleton variant="rectangular" sx={{ maxWidth: "100%", minHeight: "50&" }} />
      <Skeleton variant="rectangular" sx={{ maxWidth: "100%", minHeight: "50%" }} />
      <Skeleton variant="rectangular" sx={{ maxWidth: "100%", minHeight: "50%" }} />
      <Skeleton variant="rectangular" sx={{ maxWidth: "100%", minHeight: "50%" }} />
      <Skeleton variant="rectangular" sx={{ maxWidth: "100%", minHeight: "50&" }} />
      <Skeleton variant="rectangular" sx={{ maxWidth: "100%", minHeight: "50%" }} />
      <Skeleton variant="rectangular" sx={{ maxWidth: "100%", minHeight: "50%" }} />
    </Stack>
  );
}

export default SkeletonTable;
