<template>
  <div class="flex-box wrapper">
    <h1>Reversi Game</h1>
    <div class="board" v-for="(row, i) in board" :key="i">
      <div class="board-row" v-for="(element, j) in row" :key="j">
        <button @click="place(i, j)">
          {{ this.board[i][j] ? (this.board[i][j] == 1 ? "⚪" : "⚫") : "" }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { isProxy, toRaw } from "vue"
export default {
  name: "ReversiGame",
  props: {},
  data: () => ({
    board: null,
    turn: 1,
  }),
  created() {
    this.fetchBoard().catch((e) => {
      console.error(e)
    })
  },
  methods: {
    async fetchBoard() {
      const res = await fetch("http://localhost:5000/board")
      const data = await res.json()
      this.board = isProxy(data) ? toRaw(data) : data
    },
    async place(y, x) {
      const res = await fetch("http://localhost:5000/place", {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify({ player: this.turn % 2, locs: [y, x] }),
      })
      const data = await res.json()
      this.board = isProxy(data) ? toRaw(data) : data

      this.turn++
    },
  },
}
</script>

<style>
body {
  font-family: Verdana;
}
.flex-box {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}
.wrapper {
  width: 100vw;
  text-align: center;
}
.heading {
  font-size: 8rem;
}
.board {
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 80vw;
}
.board-row {
  display: inherit;
  flex-direction: column;
}
.board button {
  width: 1.8rem;
  height: 1.8rem;
  background-color: #50c878;
}
</style>
