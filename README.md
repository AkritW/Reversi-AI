# About

Reversi is a strategic board game played on an 8×8 uncheckered board.

The rules are simple.

1. Each player take their turn to place a disks on the board.
2. Any disks of the opponent's color that are in a straight line and bounded by the disk just placed and another disk of the current player's color are turned over to the current player's color.
3. Whoever get end up with the highest number of disks with their color wins.

NEAT (NeuroEvolution of Augmenting Topologies) is a reinforcement learning method developed by Kenneth O. Stanley for evolving arbitrary neural networks.

Our goal is to create a superhuman level AI with NEAT model to play in a Reversi game.

# Game Engine

Reversi engine is a custom build using Python and is represented as in the matrix below.\
The game is represented in a 8x8 matrix using numpy array.

$$
\begin{bmatrix}
\phantom{-}0 & \phantom{-}0 & \phantom{-} 0 & \phantom{-} 0 & \phantom{-} 0 & \phantom{-} 0 & \phantom{-} 0  & \phantom{-} 0 \\
\phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 \\
\phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 \\
\phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}1 & -1 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 \\
\phantom{-}0 & \phantom{-}0 & \phantom{-}0 & -1 & \phantom{-}1 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 \\
\phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 \\
\phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 \\
\phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 & \phantom{-}0 \\
\end{bmatrix}
$$

# AI Algorithm

To be written...
