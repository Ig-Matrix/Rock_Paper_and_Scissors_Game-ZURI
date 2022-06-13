# Rock_Paper_and_Scissors_Game-ZURI
Rock-Paper-Scissors is a simple two-player game where, at a signal, players make figures with their hands, representing a rock, a piece of paper, or a pair of scissors. The winner is determined according to a set of rules.
If the two players choose the same “character” it’s a tie, and the game repeats
Rock beats Scissors
Paper beats Rock
Scissors beats Paper
I created a simple version of this game with Python. In my version, one player will be controlled by the computer and the other player controlled by you - the user (i.e CPU vs Player).

The game is inside the folder titled main.py.
A list was created a list to store all possible options:
"R" for "rock",
"P" for "paper",
"S" for "scissors".
When the program is run, the user is asked to pick an option between "R", "P" or "S"
If user input is invalid (not amongst our options), an error is printed, and their input is asked for again ( a loop)
`
Check both player's moves:
If there is a winner, print the winner is printed, and the program ends.
If it's a tie (the computer and player pick the same move), the game is restarted

