import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import { CardActionArea } from "@mui/material";

function AdCard() {
  return (
    <Card
      sx={{
        background: "#BBBB",
        flexBasis: "25%",
        margin: 5,
        minWidth: "200px",
        minHeight: "200px",
      }}
    >
      <CardActionArea href="https://google.com">
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            Ads
          </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  );
}

export default AdCard;
