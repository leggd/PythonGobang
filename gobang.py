#**********************************IMPORTANT**********************************
#                                                                            #
# NOTE: IF USING IDLE SHELL, YOU MAY NEED TO EXPAND CONSOLE HORIZONTALLY     #
#                   IN ORDER TO SEE THE GAME BOARD CORRECTLY                 #
#                                                                            #
#**********************************IMPORTANT**********************************
import random

# Function to create game board
def create_board():
    # Initialise a 20x20 2D list
    empty_board = [[' ' for _ in range(20)] for _ in range(20)]
    
    # Initialise tuple of letters to label each row
    letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J',
               'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T')
    
    # Range loop for each row in the board
    for i in range(len(empty_board)):
        # Set the first box of each column as row number, adjusting right
        empty_board[i][0] = str(i).rjust(2)
        
    # Range loop for each column in the board, starting from index [1]
    for i in range(1, len(empty_board[0])):
        # Label the top row with letters 'A' to 'T'       
        empty_board[0][i] = letters[i-1]
        
    # Initialise list of '-' characters
    board_lines = ['-' for _ in range(len(empty_board[0]))]

    # Set the first character of line as empty space
    board_lines[0] = ' '

    # Join the characters in the line with ' + ' and add space at start and end
    board_lines = ' + '.join(board_lines)
    board_lines = '  ' + board_lines + ' +'

    # Initialise board variable with first line
    board = [[board_lines]]

    # Set the first character of the first line as an empty space
    board[0][0] = ' ' * 81

    # Iterate through each row in the 2d empty board list
    for row in empty_board:

        # Join characters in row with seperators then add row to board
        row_str = ' | '.join(map(str, row))
        row_str = '|' + row_str + ' |'
        board.append([c for c in row_str])

        # Add a line to the board after each row
        board.append([board_lines])

    # Set the visual top left corner to an empty space
    board[1][2] = ' '
    
    # Iterate through visual top row and set alignment
    for i in range(0,84,4):
        board[1][i] = ' '
    
    # Iterate through visual first column and set alignment
    for i in range(3,41,2):
        board[i][0] = ' '

    # Return completed board    
    return board

# Function to display the game board in console
def show_board(board):
    # Iterate through each row in the board
    for row in board:
        # Join each character in the row list into a string and print
        print(''.join(row))

# Function to handle player moves
def player_move(board,piece):
    # Initialise dictionary to map column letters to their index on board
    col_index = {'a': 6, 'b': 10, 'c': 14, 'd': 18, 'e': 22, 'f': 26, 'g': 30,
                 'h': 34, 'i': 38, 'j': 42, 'k': 46, 'l': 50, 'm': 54, 'n': 58,
                 'o': 62, 'p': 66, 'q': 70, 'r': 74, 's': 78}
    
    # Initialise dictionary to map row numbers to their index on board
    row_index = {'1': 3, '2': 5, '3': 7, '4': 9, '5': 11, '6': 13, '7': 15,
                 '8': 17, '9': 19, '10': 21, '11': 23, '12': 25, '13': 27,
                 '14': 29, '15': 31, '16': 33, '17': 35, '18': 37, '19': 39}
    
    # Loop to obtain row number input
    while True:
        move_row = input("Which row to place marker? (1-19): ")
        
        # Remove leading/trailing spaces from input
        move_row = move_row.strip()

        # Check if input is empty
        if not move_row:
            print("You didn't enter anything!")

        # Check if input is not a number
        elif not move_row.isdigit():
            print("You didn't enter a valid number!")

        else:
            # Convert the input to integer to allow comparisons
            move_row = int(move_row)

            # Check if input is less than or more than range of rows
            if move_row < 1 or move_row > 19:
                print("Out of range! (1-19)")
            
            else:
                # Convert input to string to match row index dict key type
                move_row = str(move_row)

                # Obtain true row index from dictionary
                row_sel = row_index.get(move_row)
                break

    # Loop to obtain column number input
    while True:            
        move_col = input("Which column to place marker? (A-S): ")

        # Remove leading/trailing spaces from input
        move_col = move_col.strip()

        # Check if input is empty
        if not move_col:
            print("You didn't enter anything!")
        
        # Check if input is more than 1 character
        elif len(move_col) > 1:
            print("Invalid Selection, too many characters!")

        else:
            # Initialise empty list to store letters        
            letters = []

            # Iterate through col index dictionary and extract keys
            for key in col_index:
                # Add keys to letters list
                letters.append(key)

            # Convert letters to string
            letter_str = ''.join(letters)

            # Convert input to lower case
            move_col = move_col.lower()

            # Check if input is not in string of letters
            if move_col not in letter_str:
                print("Invalid Selection, not in range! (A-S)")
            else:
                # Obtain true row index from dictionary
                col_sel = col_index.get(move_col)
                break
    
    # Check if the selected position on board is empty
    if board[row_sel][col_sel] == ' ':
        # Place piece on board at selected position
        board[row_sel][col_sel] = piece
        return True
    else:
        print("Position is occupied, please choose another!")

# Function to check for winner
def win_check(board, piece):
    # Vertical Win Check, iteration through columns
    for col in range(6,79,4):
        # Convert column into string for analysis
        col_str = ''.join(board[row][col] for row in range(3,36,2))

        # Check if there is 5 pieces in the current column string
        if col_str.count(piece * 5) > 0:

            # Initialise empty winning index list
            winning_indicies = []

            # Iteration through rows
            for row in range(3, 36, 2):

                # Check for piece in individual location
                if board[row][col] == piece:

                    # Store index of piece as tuple
                    winning_indicies.append((row,col))

                    # Stop logging indicies after 5 found
                    if len(winning_indicies) == 5:

                        # Return win state boolean and indicies to main loop
                        return True, winning_indicies
                else:
                    # Reset list to stop non-winning indicies being stored
                    winning_indicies = []

    # Horizontal Win Check, iteration through rows
    for row in range(3, 36, 2):

        # Convert row into string for analysis
        row_str = ''.join(board[row][col] for col in range(6, 79, 4))

        # Check if there is 5 pieces in the current row string
        if row_str.count(piece * 5) > 0:

            # Initialise empty winning index list
            winning_indicies = []

            # Iteration through columns
            for col in range(6,79,4):

                # Check for piece in individual location
                if board[row][col] == piece:

                    # Store index of piece as tuple
                    winning_indicies.append((row,col))

                    # Stop logging indicies after 5 found
                    if len(winning_indicies) == 5:

                        # Return win state boolean and indicies to main loop
                        return True, winning_indicies
                else:
                    # Reset list to stop non-winning indicies being stored
                    winning_indicies = []

    # Ascending Diagonal Win Check, reverse iteration through rows
    for row in range(41, 2, -2):

        # Iteration through columns
        for col in range(6, 79, 4):
            
            # Try/Except block to error handle going out of bounds
            try:

                # Check diagonal indicies for 5 pieces matching
                if (board[row][col] == piece and
                    board[row-2][col+4] == piece and
                    board[row-4][col+8] == piece and
                    board[row-6][col+12] == piece and
                    board[row-8][col+16] == piece):

                    # If match found, store winning indicies
                    winning_indicies = [(row, col),
                                        (row-2, col+4),
                                        (row-4, col+8),
                                        (row-6, col+12),
                                        (row-8, col+16)]
                    
                    # Return win state boolean and indicies to main loop
                    return True, winning_indicies
                
            except IndexError:
                continue
            
    # Descending Diagonal Win Check, iteration through rows
    for row in range(3, 41, 2):
        
        # Iteration through columns
        for col in range(6, 79, 4):

            # Try/Except block to error handle going out of bounds
            try:

                # Check diagonal indicies for 5 pieces matching
                if (board[row][col] == piece and
                    board[row+2][col+4] == piece and
                    board[row+4][col+8] == piece and
                    board[row+6][col+12] == piece and
                    board[row+8][col+16] == piece):

                    # If match found, store winning indicies
                    winning_indicies = [(row, col),
                                        (row+2, col+4),
                                        (row+4, col+8),
                                        (row+6, col+12),
                                        (row+8, col+16)]
                    
                    # Return win state boolean and indicies to main loop
                    return True, winning_indicies
                
            except IndexError:
                continue
    
    # Return false win state boolean to main loop
    return False

# Function to check if board is full
def full_check(board):

    # Iteration through rows
    for row in range(3, 41, 2):

        # Iteration through columns
        for col in range(6, 79, 4):

            # Check if board space is empty
            if board[row][col] == ' ':

                # Return false/not full state to main loop
                return False
            
    # Return true/full state to main loop if no empty spaces (' ')
    return True

# Function to obtain player names
def get_players():
    player_1_name = input("Player 1, Please enter your name: ")
    player_1_name = player_1_name.strip()

    player_2_name = input("Player 2, Please enter your name: ")
    player_2_name = player_2_name.strip()
    
    # Return default name 'Player 1' and Player 2 input name
    if not player_1_name and player_2_name:
        return 'Player 1', player_2_name 
    
    # Return Player 1 input name and default name 'Player 2'
    if player_1_name and not player_2_name:
        return player_1_name, 'Player 2'
    
    # Return both default names if players don't input
    if not player_1_name and not player_2_name:
        return 'Player 1', 'Player 2'
    
    # Return both selected names if players have input
    if player_1_name and player_2_name:
        return player_1_name, player_2_name

# Main Game Loop
def main():
    while True:
        # Initialise Game Variables
        game_over = False
        player_turn = None
        current_player = None

        BLACK_PIECE = str(chr(9679))
        WHITE_PIECE = str(chr(9675))

        # Welcome Message
        print("Welcome to Gobang!")
        
        # Obtain player names (default or custom)
        name_1, name_2 = get_players()

        # Initialise gobang board
        board = create_board()

        # Initialise player list
        players = [{'name':name_1,'piece':BLACK_PIECE},
                {'name':name_2,'piece':WHITE_PIECE}]

        # Set random first player to take turn
        player_turn = random.choice([True, False])

        # Game Loop
        while not game_over:
            # Show current state of board
            show_board(board)

            # Check if board is full and print message and end game
            if full_check(board):
                show_board(board)
                print("It's a draw!")
                game_over = True

            # Swap player profile based on player_turn value
            if player_turn:
                current_player = players[0]
            else:
                current_player = players[1]

            # Announce Turn
            print(current_player['name']+"'s Turn")

            # Obtain and execute player move
            player_move(board, current_player['piece'])

            # Check for win and replace pieces to mark winning combo if won
            if win_check(board, current_player['piece']):
                winning_places = win_check(board, current_player['piece'])[1]
                for index in winning_places:
                    row, col = index
                    board[row][col] = 'X'
                show_board(board)

                print(current_player['name']+' Wins!')

                # End the game
                game_over = True

            # Switch turns if there are no game ending conditions
            player_turn = not player_turn

        # Play Again Loop
        while True:
            play_again = input("Do you want to play again? (Y/N): ")

            play_again = play_again.strip()
            play_again = play_again.lower()
            
            if play_again == 'n':
                print("Thank you for playing!")
                return
            
            elif play_again == 'y':
                break

            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
        
if __name__ == "__main__":
    main()
