# Command-Line-Solitaire
 Play klondike solitaire on your terminal! 

## Instructions
### Downloading and launching the game
To get started, download the `klondike.py` and `card.py` files and place them in the same directory. Then, navigate to that directory in your terminal and launch the game by typing `python klondike.py`. The game should start at this point by asking you for a seed (if it did not, check to make sure that you have the latest version of python installed and that the python installation directory is in your system's PATH variable).

### Gameplay
When first started, the game will ask for a seed. At this point, you can enter any number you like and the game will base the deck randomization on that seed. This means that if you want to try the exact same game state again (maybe you realized just a *little bit* too late that you could have won), you can input that same seed and get the same deck order as before. If you don't care about that, you can simply press enter and the game will generate (and disaply) a random seed).

To play, you input your commands via text. The 7 main stacks that you can use to move cards around are represented by the numbers 1-7 (left to right) while the four stacks that store cards of each suit are represented by 'q', 'w', 'e', and 'r' (left to right). In order to access the top card of the discard pile, use 'd'. To deal a card from the deck to the discard pile, simply press enter without typing a command. The basic structure of a command is: \[stack you are moving to]\[stack you are moving from]\[how many cards to move (optional; if omitted, defaults to 1)]. As an example, say you wanted to move two cards from stack 1 to stack 6. You would type:

```162```

* 1 = starting at stack 1
* 6 = moving to stack 6
* 2 = move two cards

Here are a few more examples:

| Command        | Effect           |
| ------------- |-------------|
| 324      | Moves 4 cards from stack 3 to stack 2. |
| 15      | Moves 1 card from stack 1 to stack 5.      |
| dw | Moves a card from the discard pile to the second ending stack.      |
| | An empty input draws a card from the deck to the discard pile. If the deck is empty, it replaces it with the discard pile.|

You can also type `help` at any point as a command in order to see the instructions in-game.
