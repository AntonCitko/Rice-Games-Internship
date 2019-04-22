import random

class Game:
    def __init__(self, player1, player2, rounds):
        self.player1 = player1
        self.player2 = player2
        self.tot_rounds = rounds
        self.cur_round = 0
        
        self.last_winner = 0
        self.consec_wins = 0
        
    def start_game(self):
        while self.cur_round < self.tot_rounds:
            print("Round", self.cur_round + 1, "of", self.tot_rounds)
            
            p1_choice = self.player1.prompt_turn()
            p2_choice = self.player2.prompt_turn()
            
            while p1_choice == p2_choice:
                print("Both players had same choice, try again.")
                p1_choice = self.player1.prompt_turn()
                p2_choice = self.player2.prompt_turn()
            
            if p1_choice == "rock" and p2_choice == "scissors":
                self.p1_win(p1_choice, p2_choice)
            
            if p1_choice == "rock" and p2_choice == "paper":
                self.p1_lose(p1_choice, p2_choice)
                
            if p1_choice == "paper" and p2_choice == "rock":
                self.p1_win(p1_choice, p2_choice)
            
            if p1_choice == "paper" and p2_choice == "scissors":
                self.p1_lose(p1_choice, p2_choice)
                
            if p1_choice == "scissors" and p2_choice == "paper":
                self.p1_win(p1_choice, p2_choice)
            
            if p1_choice == "scissors" and p2_choice == "rock":
                self.p1_lose(p1_choice, p2_choice)
            
            print(self.player1.name, "has", self.player1.score, "and", self.player2.name, "has", self.player2.score)
            
            self.cur_round = self.cur_round + 1
        
    def p1_win(self, p1_choice, p2_choice):
        print(self.player1.name, "'s ", p1_choice, " beats ", self.player2.name, "'s ", p2_choice,sep = "")
        
        if self.last_winner == 1:
            self.consec_winner = self.consec_winner + 1
        else:
            self.last_winner = 1
            self.consec_winner = 1
            
        if self.consec_winner >= 7:
            self.player1.score = self.player1.score + 3
        elif self.consec_winner == 6:
            self.player1.score = self.player1.score + 2.5
        elif self.consec_winner == 5:
            self.player1.score = self.player1.score + 2
        elif self.consec_winner == 4:
            self.player1.score = self.player1.score + 1.8
        elif self.consec_winner == 3:
            self.player1.score = self.player1.score + 1.5
        elif self.consec_winner == 2:
            self.player1.score = self.player1.score + 1.2
        else:
            self.player1.score = self.player1.score + 1
        
        
    def p1_lose(self, p1_choice, p2_choice):
        print(self.player1.name, "'s ", p1_choice, " loses to ", self.player2.name, "'s ", p2_choice,sep = "")
        
        if self.last_winner == 2:
            self.consec_winner = self.consec_winner + 1
        else:
            self.last_winner = 2
            self.consec_winner = 1
        
        if self.consec_winner >= 7:
            self.player2.score = self.player2.score + 3
        elif self.consec_winner == 6:
            self.player2.score = self.player2.score + 2.5
        elif self.consec_winner == 5:
            self.player2.score = self.player2.score + 2
        elif self.consec_winner == 4:
            self.player2.score = self.player2.score + 1.8
        elif self.consec_winner == 3:
            self.player2.score = self.player2.score + 1.5
        elif self.consec_winner == 2:
            self.player2.score = self.player2.score + 1.2
        else:
            self.player2.score = self.player2.score + 1

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
        print(self.name, "what would you like to play (rock, paper, or scissors)")
        self.m_current = input()
        while self.m_current != "rock" and self.m_current != "paper" and self.m_current != "scissors":
            print("You must choose from the choices (rock, paper, or scissors)")
            self.m_current = input()
        
        return(self.m_current)
        

p1 = input("What is Player 1's name? ")
p2 = input("What is Player 2's name? ")
rounds = input("How many rounds would you like to play? ")
try:
    rounds = int(rounds)
except ValueError:
    print("Rounds must be an integer")

g1 = Game(Player(p1), Player(p2), rounds)

g1.start_game()


















