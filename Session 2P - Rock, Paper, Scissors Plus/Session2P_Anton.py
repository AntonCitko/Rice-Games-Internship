import random

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        
    def start_game(self):
        # game loop
        pass

   
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.m_current = "NA"
        
        # How many consecutive turns have had the same move
        # Resets to 1 evertime a new move is played
        # Adds one if same move from previous turn is played 
        self.prev_same_moves = 0
        
    def prompt_turn(self):
        pass
        

g1 = Game(Player(input("What is Player 1's name? ")), Player(input("What is Player 2's name? ")))


















