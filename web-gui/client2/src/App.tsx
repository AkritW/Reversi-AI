import React, { useState, useEffect } from "react"
import { QueryClient, QueryClientProvider, useQuery } from "react-query"
import { MantineProvider, createStyles, Box, Button } from "@mantine/core"

const queryClient = new QueryClient()

const useStyles = createStyles((theme, _params, getRef) => ({
  a: "a",
}))

const App = () => {
  return (
    <MantineProvider
      theme={{
        colorScheme: "dark",
        respectReducedMotion: true,
        white: "#dddddd",
        black: "#282c34",
      }}
    >
      <QueryClientProvider client={queryClient}>
        <MainContent />
      </QueryClientProvider>
    </MantineProvider>
  )
}

const MainContent = () => {
  const { isLoading, error, data } = useQuery("board", () =>
    fetch("http://localhost:5000/board").then((res) => res.json())
  )

  return (
    <div className="App">
      <h1>Reversi</h1>
      {data &&
        data.map((row, y) => {
          return (
            <Box
              style={{
                display: "flex",
                flexDirection: "row",
                justifyContent: "center",
                alignItems: "center",
              }}
              key={y}
            >
              {row.map((e, x) => {
                return (
                  <Button size="xl" key={y.toString() + x.toString()}>
                    {e == 1 ? "⚫" : e == -1 ? "⚪" : e == 2 ? "🟢" : ""}
                  </Button>
                )
              })}
            </Box>
          )
        })}
    </div>
  )
}

export default App
