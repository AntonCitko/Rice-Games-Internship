# Rock, Paper, Scissors+

## The Game

Rock, Paper, Scissors+ is a new take on the classic game from which it gets its name. Its structure remains the same, that is, two players each choose rock, paper, or scissors and then reveal their choice at the same time. Rock crushes scissors, scissor cuts paper, and paper covers rock. This is done for a number of rounds, traditionally, best of three.

This version of the game has a number of additional components that make it more interesting:

- The game is based on a point system where winning streaks increase the number of points the winner receives.
- If a player has won 3 or 6 times in a row, their options for the next round are only the move they played in the last round and one random option generated from the remaining moves
- If a player has played the same for the last 3 rounds, their score gets doubled on the next round.

### Scoring Multiplier

| Consecutive Wins | Score Multiplier |
|------------------|------------------|
| 2                | 1.2x             |
| 3                | 1.5x             |
| 4                | 1.8x             |
| 5                | 2x               |
| 6                | 2.5x             |
| 7+               | 3x               |  

### Image of game

![RPS+](https://github.com/antonqp/Rice-Games-Internship/blob/master/Session%202P%20-%20Rock%2C%20Paper%2C%20Scissors%20Plus/RPS%2B%20In%20Game.png)

The game is all text based. Each round the user types in the move they would like to play based on the options presented. It plays until the number of rounds initially specified is reached.

## Code

The programming behind the game is built behind two classes: `Game` and `Player`.

### Game
This object contains a number of key variables: two player objects, the total number of rounds, the current round, who the last winner was, and the number of consecutive wins that winner has.

To initialize a game, the `start_game` function is called. This uses the built-in prompt functions for each player to ask for their choices. From there, `start_game` checks who the won the round and then calls either `p1_win` or `p1_lose` depending on who won. `p1_win` and `p1_lose` function the same, but print differing messages that announce who won the round. Each function, calculates the proper score to give the winner based on the consecutive wins and previous moves. Additionally it updates the `last_winner` and `consec_wins` values for `Game`.

### Player

The `Player` Object stores each players information that `Game` uses, the player's name, their score, the current move, and the number of times they played the same move.

The only function in `Player` is `prompt_turn`. This function takes in a boolean that tells the function whether or not to reduce the number of choices the player has, which occurs if they have won the last 3 or 6 rounds in a row. `m_current` is useful here because it tells the program the first option the player has, then the other option is selected using a random number. If the player has not won the last 3 to 6 rounds consecutively, the function allows the player to choose from any of the three moves.
