import { Button, Paper, Stack, TextareaAutosize } from "@mui/material";

export const QuestionBox = () => {
  return (
    <Paper elevation={2} style={{ padding: "16px" }}>
      <Stack
        spacing={1}
        direction="row"
        alignItems="center"
        justifyContent="center"
      >
        <TextareaAutosize
          style={{
            width: "100%",
          }}
          minRows={5}
          placeholder="Ask your questions here!"
        />
        <Button
          variant="contained"
          size="large"
          style={{
            minHeight: "100%",
            height: "100%",
          }}
        >
          Send
        </Button>
      </Stack>
    </Paper>
  );
};
