import React from "react";
import { Container, Stack, TextareaAutosize } from "@mui/material";
import { QuestionList } from "../components/QuestionList";

export const Room = () => {
  return (
    <Container>
      <Stack spacing={2}>
        <TextareaAutosize minRows={5} placeholder="Ask your questions here!" />
        <QuestionList />
      </Stack>
    </Container>
  );
};
