import React, { useState, useEffect } from "react"
import {
  QueryClient,
  QueryClientProvider,
  useQuery,
  useMutation,
} from "react-query"
import {
  MantineProvider,
  createStyles,
  Box,
  Button,
  Title,
  Text,
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
    flexDirection: "row",
  },
  board: {
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
  additionalInfo: {
    display: "flex",
    flexDirection: "column",
    fontFamily: "Montserrat",
    color: "#fff",
  },
  turn: {
    marginBottom: 80,
  },
  whiteScore: {
    marginBottom: 80,
  },
  blackScore: {
    marginBottom: 80,
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
  // Styling for Mantine Components
  const { classes } = useStyles()

  // State is needed to mutate both GET and POST
  const [data, setData] = useState()

  // query board and display
  const { isLoading } = useQuery(
    "board",
    () => fetch("http://localhost:5000/board").then((res) => res.json()),
    {
      onSuccess: (data) => setData(data),
    }
  )

  // post location and update board
  const { mutate } = useMutation("board", placeDisk)
  const place = (player, locs) => {
    mutate(
      { player, locs },
      {
        onSuccess: (data) => setData(data),
      }
    )
  }

  // debugging purposes
  useEffect(() => {
    console.log(data)
  }, [data])

  return (
    <Box className="App">
      <Box className={classes.main}>
        <Title className={classes.heading}>REVERSI</Title>
        <Box className={classes.boardWrapper}>
          <Box className={classes.board}>
            {!isLoading &&
              data.board.map((row, y) => {
                return (
                  <Box className={classes.boardRow} key={y}>
                    {row.map((e, x) => {
                      return (
                        <Button
                          className={classes.square}
                          size="xl"
                          key={y.toString() + x.toString()}
                          onClick={() => place(data.player, [y, x])}
                        >
                          <Disk val={e} player={data.player} />
                        </Button>
                      )
                    })}
                  </Box>
                )
              })}
          </Box>
          <Box className={classes.additionalInfo}>
            <Box className={classes.turn}>
              <Text style={{ fontSize: 20, fontWeight: "bold" }}>Turn</Text>
              <Text style={{ fontSize: 30, fontWeight: "bold" }}>
                {data && data.player ? "White" : "Black"}
              </Text>
            </Box>
            <Box className={classes.whiteScore}>
              <Text style={{ fontSize: 20, fontWeight: "bold" }}>
                {"Black's score"}
              </Text>
              <Text style={{ fontSize: 30, fontWeight: "bold" }}>
                {data && data.blackScore}
              </Text>
            </Box>
            <Box className={classes.blackScore}>
              <Text style={{ fontSize: 20, fontWeight: "bold" }}>
                {"White's score"}
              </Text>
              <Text style={{ fontSize: 30, fontWeight: "bold" }}>
                {data && data.whiteScore}
              </Text>
            </Box>
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
  const diskMapper = (val, player) => {
    switch (val) {
      case 0:
        return ""
      case 1:
        return classes.whiteDisk
      case 2:
        return classes.blackDisk
      case 3:
        return player ? classes.validWhite : classes.validBlack
      default:
        return "NA"
    }
  }

  return <Box className={diskMapper(props.val, props.player)} />
}

interface PlaceInfo {
  player: number
  board: Array<number>
}
const placeDisk = async (placeInfo: PlaceInfo) => {
  return await fetch("http://localhost:5000/place", {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify({ player: placeInfo.player, locs: placeInfo.locs }),
  }).then((res) => res.json())
}
export default App
