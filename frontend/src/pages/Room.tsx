import { Container, Stack } from "@mui/material";
import { QuestionBox } from "../components/QuestionBox";
import { QuestionList } from "../components/QuestionList";

export const Room = () => {
  return (
    <Container style={{ padding: "16px", height: "100%" }}>
      <Stack spacing={2}>
        <QuestionBox />
        <QuestionList />
      </Stack>
    </Container>
  );
};
