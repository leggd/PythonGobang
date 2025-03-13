Gobang (Five in a Row) Game

Welcome to the Gobang game! This is a Python-based implementation of the classic game of Gobang (also known as Gomoku or Five-in-a-Row).
The game is designed for two players, and the objective is to be the first to get five of your pieces in a row, either horizontally, vertically, or diagonally.

Features
--------
- 2D Game Board: The game is played on a 20x20 board, with each player trying to place five of their pieces consecutively.
- Customizable Player Names: Players can input their names, or default names will be used.
- Piece Representation: Black pieces are represented by "●" (Unicode character U+25CB), and white pieces are represented by "○" (Unicode character U+25CB).
- Game Flow: The game alternates turns between Player 1 and Player 2, checking for a win after every move.
- Win Condition: The game checks for five consecutive pieces either horizontally, vertically, or diagonally.
- Draw Condition: If the board is full and no one has won, the game ends in a draw.

Installation
------------
To play the game, simply clone the repository and run the Python script.

1. Clone the repository:
   git clone https://github.com/leggd/pythongobang.git
2. Navigate to the game directory:
   cd gobang
3. Run the game:
   python gobang.py

How to Play
-----------
1. Start the Game: Run the script, and the game will prompt you to enter names for Player 1 and Player 2. If no name is provided, default names will be used.
2. Making Moves: Players take turns entering their move:
   - Row: Enter the row number (1-19) where you want to place your piece.
   - Column: Enter the column letter (A-S) where you want to place your piece.
3. Winning: The game will announce the winner if a player successfully places five pieces in a row. 
4. Draw: If the board is filled without a winner, the game will end in a draw.
5. Game Reset: The game will restart automatically after a game ends.


Contributions
-------------
Feel free to fork this project and contribute improvements or fixes. 


Credits
-------
Daniel Legg (Created as an assignement in Foundation Year for 'Computational Thinking & Mathematics' module
