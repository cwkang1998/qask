import React from "react";
import { Button, Container, Stack, TextareaAutosize } from "@mui/material";
import { QuestionList } from "../components/QuestionList";

export const Room = () => {
  return (
    <Container style={{ padding: "16px", height: "100%" }}>
      <Stack spacing={2}>
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
              height: "100%",
            }}
          >
            Send
          </Button>
        </Stack>

        <QuestionList />
      </Stack>
    </Container>
  );
};
