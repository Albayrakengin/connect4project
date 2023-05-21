import sys
import pygame
import menu
import user
from time import sleep
import conditions 
# Set the dimensions of the game board
board_width = 720
board_height = 720
global current_player
# Set the dimensions of each cell on the board
cell_size = 80

# Set the number of rows and columns on the board
num_rows = board_height // cell_size
num_cols = board_width // cell_size

# Create the game board
game_board = [[0] * num_cols for _ in range(num_rows)]

# Define the colors used in the game
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Set the background color of the game window
background_color = WHITE

# Set the dimensions of the game window
window_width = board_width
window_height = board_height + 50

# Create the game window
game_window = pygame.display.set_mode((window_width, window_height))

# Set the title of the game window
pygame.display.set_caption("Connect Four")

ussample = user.user_data()

# Draw the game board
def draw_board():
    for row in range(num_rows):
        for col in range(num_cols):
            pygame.draw.rect(game_window, WHITE, (col * cell_size, row * cell_size + 50, cell_size, cell_size))
            pygame.draw.line(game_window, BLACK, (col * cell_size, 50), (col * cell_size, board_height + 50))
            pygame.draw.line(game_window, BLACK, (0, row * cell_size + 50), (board_width, row * cell_size + 50))

            if game_board[row][col] == 1:
                pygame.draw.circle(game_window, RED, (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2 + 50), cell_size // 2 - 5)
            elif game_board[row][col] == 2:
                pygame.draw.circle(game_window, BLACK, (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2 + 50), cell_size // 2 - 5)


def update_array():
    temp_black = []
    temp_red = []
    # Iterate over the game board array and check each cell
    for row in range(num_rows):
        for col in range(num_cols):
            if game_board[row][col] == 1:
                # If there is a circle in this cell, add its coordinates to the list
                temp_red.append((row,col))
            elif game_board[row][col] == 2:
                temp_black.append((row,col))
    ussample.black_moves = temp_black
    ussample.red_moves = temp_red
    tableInfo = ussample.gameBoard_to_dict(game_board)
    movesInfo = ussample.moves_to_dict()
    ussample.save_dict(tableInfo, "table")
    ussample.save_dict(movesInfo,"moves")
                

def show_menu():
    global game_board
    pygame.init()
    ussample.read_data()

    # Create a text input for each player to enter their name
    player1_input = menu.TextInput(300, 200, 200, 50, "Red Player:")
    player2_input = menu.TextInput(300, 300, 200, 50, "Black Player:")

    # Define a variable to keep track of whether the menu is currently displayed
    menu_displayed = True

    while menu_displayed:
        # Handle events for the menu
        for event in pygame.event.get():
            player1_input.handle_event(event)
            player2_input.handle_event(event)       
                     
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the user clicked the "Start" button
                if start_button.is_clicked():
                    # Get the names entered by the players
                    player1_name = player1_input.get_text()
                    player2_name = player2_input.get_text()

                    # Start the game with the player names as parameters
                    ussample.black_user = player2_name
                    ussample.red_user = player1_name

                    # Decide who is going to be red
                    message = menu.Button.pick_color(player1_name, player2_name)
                    result_button = menu.Button(400, 400, 200, 50, message)
                    result_button.draw(game_window)
                    pygame.display.update()
                    sleep(2)

                    # Pass to game window
                    start_table(player1_name, player2_name ,ussample.last_player)
                elif continue_index:
                    if continue_button.is_clicked():
                        game_board = ussample.gameBoard 
                        start_table(ussample.red_user, ussample.black_user ,ussample.current_player)

        # Draw the menu elements
        game_window.fill((255, 255, 255))
        menu.TextInput(200, 200, 100, 100, "Connect 4")
        player1_input.draw(game_window)
        player2_input.draw(game_window)
        start_button = menu.Button(200, 400, 100, 50, "Start")
        start_button.draw(game_window)
        if ussample.has_stared:
            continue_index = True
            continue_button = menu.Button(200, 475, 100, 50, "Continue")
            continue_button.draw(game_window)
        else:
            continue_index = False
        # Update the display
        pygame.display.update()

def start_table(player1, player2, current_player):
    ussample.has_stared = 1
    # Main game loop
    while True:
        pygame.init()

        if current_player == 1:
            pygame.display.set_caption(player1)
        elif current_player == 2:
            pygame.display.set_caption(player2)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the column where the player clicked
                col = event.pos[0] // cell_size
                # Find the lowest empty row in the column
                row = num_rows - 1
                while row >= 0:
                    if game_board[row][col] == 0:
                        break
                    row -= 1
                # If the column is full, do nothing
                if row < 0:
                    pass
                # Update the game board and draw a red circle in the cell
                #game_board[row][col] = 1
                if current_player == 1 and game_board[row][col] == 0:
                # If the current player is 1, draw a red circle
                    game_board[row][col] = 1
                    ussample.last_player = 1
                    current_player = 2
                    ussample.current_player = 2
                elif current_player == 2 and game_board[row][col] == 0:
                    # If the current player is 2, draw a black circle
                    game_board[row][col] = 2
                    ussample.last_player = 2
                    current_player = 1
                    ussample.current_player = 1
                update_array()
                sample = conditions.conditions()

                #winning condition
                try:
                    while (sample.winning_move(ussample.last_player)):
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.display.quit()
                                pygame.quit()

                        winner = [ussample.red_user, ussample.black_user]
                        pygame.display.set_caption(f'winner is {winner[ussample.last_player - 1]}')
                        game_window.fill((255, 255, 255))
                        winner = ["red","black"]
                        winner_button = menu.Button(250, 360, 200, 100, f'the winner is {winner[ussample.last_player - 1]}')
                        winner_button.draw(game_window)
                        pygame.display.update()   
                except:
                    pass
                #draw condition
                try:
                    while (sample.tie_move()):
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.display.quit()
                                pygame.quit()
                                exit()

                        pygame.display.set_caption("It's tie!")
                        game_window.fill((255, 255, 255))
                        tie_button = menu.Button(360, 360, 200, 100, f'The game is draw')
                        tie_button.draw(game_window)
                        pygame.display.update()   
                except:
                    pass

                 
            
        # Draw the game board
        draw_board()
        pygame.display.update()