<template>
  <div
    style="
      display: flex;
      justify-content: center;
      flex-direction: column;
      width: 100vw;
      margin-bottom: 5vw;
    "
  >
    <h1
      style="
        text-align: center;
        font-weight: bold !important;
        margin-top: 4vw !important;
        margin-bottom: 3vw !important;
      "
    >
      Reversi Game
    </h1>
    <div
      style="
        display: flex;
        flex-direction: row;
        width: auto;
        align-items: center;
        justify-content: center;
      "
    >
      <div
        style="display: flex; flex-direction: column; width: auto"
        v-for="(row, i) in board"
        :key="i"
      >
        <div
          style="
            width: 4.5vw;
            height: 4.5vw;
            margin: 0;
            padding: 0;
            border-width: 0.15vw;
            border-radius: 0.5vw;
            border-style: solid;
          "
          v-for="(element, j) in row"
          :key="j"
        >
          <button
            class="btn btn-secondary"
            style="width: 4.5vw; height: 4.5vw; font-size: 2.4vw"
            @click="place(i, j)"
          >
            {{ this.board[i][j] ? (this.board[i][j] == 1 ? "⚪" : "⚫") : "" }}
          </button>
        </div>
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
/* body { */
/*   font-family: Verdana; */
/* } */
/* .flex-box { */
/*   display: flex; */
/*   justify-content: center; */
/*   flex-direction: column; */
/*   align-items: center; */
/* } */
/* .wrapper { */
/*   width: 100vw; */
/*   text-align: center; */
/* } */
/* .heading { */
/*   font-size: 8rem; */
/* } */
/* .board { */
/*   display: flex; */
/*   flex-direction: row; */
/*   justify-content: center; */
/*   width: 80vw; */
/* } */
/* .board-row { */
/*   display: inherit; */
/*   flex-direction: column; */
/* } */
/* .board button { */
/*   width: 1.8rem; */
/*   height: 1.8rem; */
/*   background-color: #50c878; */
/* } */
body {
  height: 100%;
  /* max-height: 600px; */
  width: 1000px;
  background-color: hsla(200, 40%, 30%, 0.4);
  background-image: url("https://78.media.tumblr.com/cae86e76225a25b17332dfc9cf8b1121/tumblr_p7n8kqHMuD1uy4lhuo1_540.png"),
    url("https://78.media.tumblr.com/66445d34fe560351d474af69ef3f2fb0/tumblr_p7n908E1Jb1uy4lhuo1_1280.png"),
    url("https://78.media.tumblr.com/8cd0a12b7d9d5ba2c7d26f42c25de99f/tumblr_p7n8kqHMuD1uy4lhuo2_1280.png"),
    url("https://78.media.tumblr.com/5ecb41b654f4e8878f59445b948ede50/tumblr_p7n8on19cV1uy4lhuo1_1280.png"),
    url("https://78.media.tumblr.com/28bd9a2522fbf8981d680317ccbf4282/tumblr_p7n8kqHMuD1uy4lhuo3_1280.png");
  background-repeat: repeat-x;
  background-position: 0 20%, 0 100%, 0 50%, 0 100%, 0 0;
  background-size: 2500px, 800px, 500px 200px, 1000px, 400px 260px;
  animation: 50s para infinite linear;
}

@keyframes para {
  100% {
    background-position: -5000px 20%, -800px 95%, 500px 50%, 1000px 100%,
      400px 0;
  }
}
</style>
