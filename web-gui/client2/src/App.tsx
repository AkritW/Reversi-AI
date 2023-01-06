import React, { useState, useEffect } from "react"
import { QueryClient, QueryClientProvider, useQuery } from "react-query"
import {
  MantineProvider,
  createStyles,
  Box,
  Button,
  Title,
} from "@mantine/core"

const queryClient = new QueryClient()

const useStyles = createStyles((theme, _params, getRef) => ({
  main: {
    top: 0,
    left: 0,
    backgroundColor: "#2E2E2E",
    width: "100vw",
    height: "100vh",
  },
  heading: {
    fontFamily: "Montserrat",
    fontStyle: "normal",
    fontWeight: 700,
    fontSize: 64,
    color: "#fff",
    textAlign: "center",
    padding: 30,
  },
  boardWrapper: {
    display: "flex",
    justifyContent: "center",
  },
  board: {
    position: "absolute",
    width: 640,
    height: 640,
    filter: "drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25))",
  },
  boardRow: {
    display: "flex",
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
  },
  square: {
    boxSizing: "border-box",
    width: 64,
    height: 64,
    background: "#51816D",
    border: "1px solid #DCDCDC",
    borderRadius: 0,
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
  },
  blackDisk: {
    width: 56,
    height: 56,
    left: 0,
    right: 0,
    top: 0,
    bottom: 0,
    background:
      "radial-gradient(50% 50% at 50% 50%, #565656 9.17%, #000000 94.06%, #343434 100%)",
    boxShadow: "0px 4px 4px rgba(0, 0, 0, 0.25)",
    borderRadius: 40,
  },
  whiteDisk: {
    width: 56,
    height: 56,
    left: 0,
    right: 0,
    top: 0,
    bottom: 0,
    background:
      "radial-gradient(50% 50% at 50% 50%, #FFFFFF 50%, #CCC9C9 100%)",
    boxShadow: "0px 4px 4px rgba(0, 0, 0, 0.25)",
    borderRadius: 40,
  },
  validBlack: {
    width: 42,
    height: 42,
    left: 0,
    right: 0,
    top: 0,
    bottom: 0,
    border: "7px solid #000",
    borderRadius: 40,
  },
  validWhite: {
    width: 42,
    height: 42,
    left: 0,
    right: 0,
    top: 0,
    bottom: 0,
    border: "7px solid #fff",
    borderRadius: 40,
  },
}))

const App = () => {
  return (
    <MantineProvider
      theme={{
        colorScheme: "dark",
        respectReducedMotion: true,
        white: "#FFFFFF",
        black: "#2E2E2E",
        globalStyles: {
          body: {
            top: 0,
            left: 0,
            margin: 0,
          },
        },
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

  const { classes } = useStyles()

  return (
    <Box className="App">
      <Box className={classes.main}>
        <Title className={classes.heading}>REVERSI</Title>
        <Box className={classes.boardWrapper}>
          <Box className={classes.board}>
            {data &&
              data.board.map((row, y) => {
                return (
                  <Box className={classes.boardRow} key={y}>
                    {row.map((e, x) => {
                      return (
                        <Button
                          className={classes.square}
                          size="xl"
                          key={y.toString() + x.toString()}
                        >
                          <Disk val={e} player={classes.player} />
                        </Button>
                      )
                    })}
                  </Box>
                )
              })}
          </Box>
        </Box>
      </Box>
    </Box>
  )
}

interface DiskProps {
  val: number
  player: number
}
const Disk = (props: DiskProps) => {
  const { classes } = useStyles()
  const diskMap = {
    "0": "",
    "1": classes.blackDisk,
    "2": classes.whiteDisk,
    "3": props.player ? classes.validWhite : classes.validBlack,
  }

  return <Box className={diskMap[props.val]} />
}

export default App
