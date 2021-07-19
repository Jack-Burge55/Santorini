# Santorini

This pygame models the basic version of the great board game Santorini, where two players (each with two builders) compete to see who can be first to place one of their builders 
on the top of a tower ( a level 3). 
## Builder Placement
First, purple selects a square on the 5x5 grid to place a builder. The players alternate until all four builders have been placed, each in a different square.
## A Standard Turn
On a players turn, they must first pick one of their builders by clicking on them. They then choose an adjacent empty square, sideways or diagonally, and click on it to move
their builder there. Now, the player must click a new adjacent square to their moved builder with no builder to "build" up a single level. The next player starts their turn.
## Moving Up or Down
A builder may move up a maximum of one level a turn on their movement, so 0 -> 1 is valid but 1 -> 3 is invalid. Further, a builder may jump down any number of squares.
## Domes
A builder may on their build phase build on a level 3 to a dome, turning it into a Santorini tower which may not be stood on. This is useful to block another players attempt to 
win by getting to the top of a level 3
## Winning
A player wins when one of their two builders reaches a level 3, or when the opposing player has no valid moves (much less likely and as of 19/7/2021 not coded into the program)
## Further Program Improvements
This was my first attempt at using Pygame, and being a relative novice I am sure this could be improved somewhat. For example, the original game comes with 30 "God Cards". Each
player selects a God before builder placement and this grants them a particular power (or their opponent a difficult restriction!). This would be a fun progression of the program
to code in.
## Credits
Made by Jack Burgess
