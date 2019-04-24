# Rock, Paper, Scissors+

## The Game

Rock, Paper, Scissors+ is a new take on the classic game from which it gets its name. Its structure remains the same, that is, two players each choose rock, paper, or scissors and then reveal their choice at the same time. Rock crushes scissors, scissor cuts paper, and paper covers rock. This is done for a number of rounds, traditionally, best of three.

This version of the game has a number of additional components that make it more interesting:

- The game is based on a point system where winning streaks increase the number of points the winner receives.  
| Consecutive Wins | Score Multiplier |
|------------------|------------------|
| 2 | 1.2x |
| 3 | 1.5x |
| 4 | 1.8x |
| 5 | 2x |
| 6 | 2.5x |
| 7+ | 3x |
- If a player has won 3 or 6 times in a row, their options for the next round are only the move they played in the last round and one random option generated from the remaining moves
- If a player has played the same for the last 3 rounds, their score gets doubled on the next round.

### Image of game

![] (URL)

The game is all text based. Each round the user types in the move they would like to play based on the options presented. It plays until the number of rounds initially specified is reached.

## Code

The programming behind the game is built behind two classes: `Game` and `Player`.

### Game
This object contains a number of key variables: two player objects, the total number of rounds, the current round, who the last winner was, and the number of consecutive wins that winner has.

To initialize a game, the `start_game` function is called. This uses the built-in prompt functions for each player to ask for their choices. From there, `start_game` checks who the won the round and then calls either `p1_win` or `p1_lose` depending on who won. `p1_win` and `p1_lose` function the same, but print differing messages that announce who won the round. Each function, calculates the proper score to give the winner based on the consecutive wins and previous moves. Additionally it updates the `last_winner` and `consec_wins` values for `Game`.

### Player

