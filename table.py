import pygame

def draw_board(game_window, game_board, cell_size):
    board_width = len(game_board[0]) * cell_size
    board_height = len(game_board) * cell_size

    for row in range(len(game_board)):
        for col in range(len(game_board[row])):
            pygame.draw.rect(game_window, (255, 255, 255), (col * cell_size, row * cell_size + 50, cell_size, cell_size))
            pygame.draw.line(game_window, (0, 0, 0), (col * cell_size, 50), (col * cell_size, board_height + 50))
            pygame.draw.line(game_window, (0, 0, 0), (0, row * cell_size + 50), (board_width, row * cell_size + 50))

            if game_board[row][col] == 1:
                pygame.draw.circle(game_window, (255, 0, 0),
                                   (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2 + 50),
                                   cell_size // 2 - 5)
            elif game_board[row][col] == 2:
                pygame.draw.circle(game_window, (0, 0, 0),
                                   (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2 + 50),
                                   cell_size // 2 - 5)

def update_board(game_board, playerData):
    tableInfo = playerData.game_board_to_dict(game_board)
    playerData.save_dict(tableInfo, "table")