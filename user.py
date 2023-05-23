import json

class UserData:
    def __init__(self) -> None:
        self.red_user:str
        self.black_user:str
        self.red_moves = []
        self.black_moves = []
        self.last_player:int
        self.has_started:bool
        self.game_board:dict
        self.current_player:int

    def game_board_to_dict(self, game_board):
        self.game_board = game_board
        sample_dict = {            
            "IsStarted" : self.has_started,
            "red": self.red_user,
            "black": self.black_user,
            "gameBoard": self.game_board,
            "lastPlayer": self.last_player,
            "currentPlayer": self.current_player
        }
        return sample_dict  


    def moves_to_dict(self):
        sample_dict = {
            "red": self.red_moves,
            "black": self.black_moves
        }
        return sample_dict


    def save_dict(self, informations, file_name):
        with open(f"{file_name}.txt", "w") as file:
            json.dump(informations, file)
    

    @staticmethod
    def clear_data():
        with open("table.txt", "w"):
            pass
    
    def user_reset(self):
        self.red_user = ""
        self.black_user = ""
        self.red_moves = []
        self.black_moves = []
        self.last_player = 0
        self.has_started = False
        self.game_board = [[0] * 9 for _ in range(9)]
        self.current_player = 0


    def read_data(self):
        try:
            with open("table.txt") as file:
                data = json.load(file)
                self.has_started = data["IsStarted"]
                self.black_user = data["black"]
                self.red_user = data["red"]
                self.game_board = data["gameBoard"]
                self.last_player = data["lastPlayer"]
                self.current_player = data["currentPlayer"]
        except:
            self.has_started = False