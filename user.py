import json

class user_data:
    def __init__(self) -> None:
        self.red_user:str
        self.black_user:str
        self.red_moves = []
        self.black_moves = []
        self.last_player:int
        self.has_stared:bool
        self.gameBoard:dict
        self.current_player:int

    def gameBoard_to_dict(self, gameBoard):
        self.gameBoard = gameBoard
        sample_dict = {            
            "IsStarted" : self.has_stared,
            "red": self.red_user,
            "black": self.black_user,
            "gameBoard": gameBoard,
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

    def save_dict(self, informations, fileName):
        with open(f'{fileName}.txt', 'w') as table:
            table.write(json.dumps(informations))
    
    def clear_data():
        with open("moves.txt",'w') as file:
            pass    
        with open("table.txt",'w') as file:
            pass    

    def read_data(self):
        try:
            with open("table.txt") as file:
                data = json.load(file)
                self.has_stared = data["IsStarted"]
                self.black_user = data["black"]
                self.red_user = data["red"]
                self.gameBoard = data["gameBoard"]
                self.last_player = data["lastPlayer"]
                self.current_player = data["currentPlayer"]
        except:
            self.has_stared = 0