import sys
import pygame
import menu
import user
import conditions
from time import sleep
from table import draw_board, update_board

# Set the dimensions of the game board
board_width = 720
board_height = 720
cell_size = 80

num_rows = board_height // cell_size
num_cols = board_width // cell_size

game_board = [[0] * num_cols for _ in range(num_rows)]

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

background_color = WHITE

# Set the dimensions of the game window
window_width = board_width
window_height = board_height + 50

game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Connect Four")

playerData = user.UserData()


def show_menu():

    global game_board
    pygame.init()
    playerData.read_data()

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
                if start_button.is_clicked():
                    player1_name = player1_input.get_text()
                    player2_name = player2_input.get_text()

                    playerData.black_user = player2_name
                    playerData.red_user = player1_name

                    message = start_button.pick_first(player1_name, player2_name)
                    result_button = menu.Button(400, 400, 200, 50, message)
                    result_button.draw(game_window)
                    pygame.display.update()
                    sleep(2)

                    # Pass to game window
                    start_table(playerData.red_user, playerData.black_user)
                elif continue_index:
                    if continue_button.is_clicked():
                        game_board = playerData.game_board
                        start_table(playerData.red_user, playerData.black_user )

        # Draw the menu elements
        game_window.fill((255, 255, 255))
        menu.TextInput(200, 200, 100, 100, "Connect 4")
        player1_input.draw(game_window)
        player2_input.draw(game_window)
        start_button = menu.Button(200, 400, 100, 50, "Start")
        start_button.draw(game_window)

        if playerData.has_started:
            continue_index = True
            continue_button = menu.Button(200, 475, 100, 50, "Continue")
            continue_button.draw(game_window)
        else:
            continue_index = False
        pygame.display.update()


def start_table(player1, player2, ):
    playerData.has_started = True
    pygame.init()

    if playerData.current_player == 1:
        pygame.display.set_caption(player1)
    elif playerData.current_player == 2:
        pygame.display.set_caption(player2)
    table_start = True
    while table_start:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                    

                col = event.pos[0] // cell_size
                row = num_rows - 1

                while row >= 0:
                    if game_board[row][col] == 0:
                        break
                    row -= 1

                if row < 0:
                    continue

                if playerData.current_player == 1 and game_board[row][col] == 0:
                    game_board[row][col] = 1
                    playerData.last_player = 1
                    playerData.current_player = 2
                    pygame.display.set_caption(playerData.black_user)
                elif playerData.current_player == 2 and game_board[row][col] == 0:
                    game_board[row][col] = 2
                    playerData.last_player = 2
                    playerData.current_player = 1
                    pygame.display.set_caption(playerData.red_user)
                
                update_board(game_board, playerData)
                sample = conditions.conditions()

                try:
                    while sample.winning_move(playerData.last_player):
                        winning_screen()
                        return
                except:
                    pass

                try:
                    while sample.tie_move():
                        tie_screen()
                        return
                except:
                    pass

        # Draw the game board
        draw_board(game_window, game_board, cell_size)
        pygame.display.update()


def tie_screen():
    global game_board
    tie = True
    while tie:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                user.UserData.clear_data()
                pygame.display.quit()
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if turn_menu.is_clicked():
                    playerData.clear_data()
                    tie = False

        pygame.display.set_caption("It's a tie!")
        game_window.fill((255, 255, 255))
        tie_button = menu.Button(250, 360, 200, 100, 'The game is a draw')
        tie_button.draw(game_window)
        turn_menu = menu.Button(500, 600, 100, 50, "Menu")
        turn_menu.draw(game_window)

        pygame.display.update()

    playerData.user_reset()
    game_board = [[0] * num_cols for _ in range(num_rows)]

def winning_screen():
    global game_board
    win_screen = True
    while win_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                user.UserData.clear_data()
                pygame.display.quit()
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    if menu_button.is_clicked():
                        win_screen = False
                        
        winner = [playerData.red_user, playerData.black_user]
        pygame.display.set_caption(f'The winner is {winner[playerData.last_player - 1]}')
        game_window.fill((255, 255, 255))
        winner = ["red", "black"]
        winner_button = menu.Button(250, 360, 200, 100, f'The winner is {winner[playerData.last_player - 1]}')
        winner_button.draw(game_window)
        menu_button = menu.Button(500, 600, 100, 50, "Menu")
        menu_button.draw(game_window)
        
        pygame.display.update()

    playerData.user_reset()
    game_board = [[0] * num_cols for _ in range(num_rows)]

