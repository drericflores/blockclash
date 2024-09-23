Block Clash
GNU General Public License

Block Clash - A puzzle board game programmed by Dr. Eric O. Flores
Copyright (C) 2024 Dr. Eric O. Flores
E-mail: eoftoro@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Block Clash game provides a simple but dynamic experience with hidden blocks, alternating turns, and a mix of strategy and luck.
Game Concept
    • Block Clash is a 2-player game (Player vs. Computer) played on a 5x5 grid (total of 25 blocks).
    • The player's goal is to click on an empty block (turning it black), while the computer randomly selects an empty block (turning it blue).
    • The game ends when either the player or the computer reaches the maximum number of points (10 points) or when all blocks on the grid are filled.
Game Flow
    • The game starts by randomly selecting who plays first: either the player or the computer.
    • On each turn, the player or the computer chooses an empty block. The player clicks a block, while the computer randomly selects one.
    • The grid is filled with black blocks (for the player) and blue blocks (for the computer).
    • Points are tracked for both the player and the computer based on how many blocks they have claimed.
Hidden "W" and "X" Blocks:
    • Two special hidden blocks exist on the grid:
        ◦ "W" Block: Gives a bonus point when clicked by either the player or the computer.
        ◦ "X" Block: Subtracts a point when clicked by either the player or the computer.
    • These blocks are placed randomly on the grid at the start of the game and are hidden. When clicked, they are re-hidden in a new random location.
Scoring and Win Condition
    • The game continues until either of these two conditions are met:
        1. A player reaches10 points.
        2. The grid is completely filled (all 25 blocks have been selected).
    • The player or computer with the most points at the end of the game is declared the winner.
Game Reset and Winner Announcement
    • When the game ends, a winner message is displayed (e.g., "Player Wins!" or "Computer Wins!").
    • The winner message flashes for a few seconds, and after8 seconds, the game resets and starts over automatically.
Detailed Breakdown of Game Components:
a)Grid Layout
    • The 5x5 grid is displayed on the screen, and each block is initially gray (un-clicked).
    • As the game progresses, clicked blocks turn black for the player or blue for the computer.
b)Turn Management
    • The game alternates turns between the player and the computer. If it’s the player's turn, they can click on an empty block. After the player clicks, the computer randomly selects a block during its turn.
    • The game keeps track of whose turn it is using theplayer_turnvariable.
c)Scoring System
    • The player_scoreand computer_score variables track how many blocks have been claimed by the player and the computer, respectively.
    • The score is displayed at the top of the screen, with the player's score on the left and the computer's score on the right.
d)Game End Logic
    • The game ends when either the player or the computer reaches10 points, or when all the blocks on the grid are filled.
    • At the end of the game, the winner is determined based on who has the most points.
e)Winner Message and Flashing Effect:
    • After the game ends, the winner message (e.g., "Player Wins!" or "Computer Wins!") flashes for a few seconds.
    • The flashing effect is controlled by toggling the visibility of the message every 500 milliseconds.
f)Automatic Reset:
    • After the game ends, there is an8-second delay(to allow time for the player to see the winner message). After this delay, the game automatically resets, and a new game begins.
    • During the reset, the grid is cleared, scores are reset to 0, and the game randomly selects whether the player or the computer starts first.
Special Features
a)Hidden "W" and "X" Blocks:
    • Hidden "W" Block: When clicked by the player or computer, it gives a bonus point.
    • Hidden "X" Block: When clicked, it deducts 1 point as a penalty.
    • These blocks move to new random positions after being clicked to keep the game dynamic.
b)Sound Effects:
    • The game plays a click sound (click.wav) each time a player clicks on a block.
    • Special sound effects are played when the "W" block (winning.wav) or "X" block (badmove.wav) is clicked, indicating the bonus or penalty.
Game Reset Mechanics:
    • At the end of each game, thereset_game()function is called to:
        ◦ Reset the grid to its initial state.
        ◦ Reset the scores to 0.
        ◦ Re-hide the "W" and "X" blocks in new positions.
        ◦ Randomly select who plays first in the new game.
Flow of Game play
    1. Game Starts: Either the player or the computer is randomly selected to play first.
    2. Player's Turn: The player clicks on an empty block, which turns black and increases their score.
    3. Computer's Turn: The computer randomly selects an empty block, which turns blue and increases its score.
    4. Hidden Block Effects: If a "W" block is clicked, the player or computer gets a bonus point. If an "X" block is clicked, the player or computer loses a point.
    5. Game Ends: When a player reaches 10 points or the grid is full, the game announces the winner and flashes the winner message.
    6. Game Reset: After an 8-second delay, the game automatically resets, and a new game begins.
