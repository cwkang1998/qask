import { Stack, TextField, Button, Grid } from "@mui/material";

export const Entry = () => {
  return (
    <Grid
      container
      direction="column"
      justifyContent="center"
      alignItems="center"
      style={{
        padding: "16px",
        height: "100%",
      }}
    >
      <Stack spacing={1}>
        <TextField label="Code" />
        <Button variant="contained">Enter</Button>
      </Stack>
    </Grid>
  );
};
