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
            
            if self.consec_wins == 3 or self.consec_wins == 6:
                if self.last_winner == 1:
                    p1_choice = self.player1.prompt_turn(True)
                    p2_choice = self.player2.prompt_turn(False)
                else:
                    p1_choice = self.player1.prompt_turn(False)
                    p2_choice = self.player2.prompt_turn(True)
            else:
                p1_choice = self.player1.prompt_turn(False)
                p2_choice = self.player2.prompt_turn(False)
            
            if p1_choice == p2_choice:
                print("Both players had same choice. It is a tie, no points.")
                self.last_winner = 0
                self.consec_winss = 0
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
            
        print("The final score is:")
        print(self.player1.name, ": ", self.player1.score, sep = "")
        print(self.player2.name, ": ", self.player2.score, sep = "")
        print("Thanks for playing!")
        
    def p1_win(self, p1_choice, p2_choice):
        print(self.player1.name, "'s ", p1_choice, " beats ", self.player2.name, "'s ", p2_choice,sep = "")
        
        if self.last_winner == 1:
            self.consec_wins = self.consec_wins + 1
        else:
            self.last_winner = 1
            self.consec_wins = 1
        
        if self.player1.prev_same_moves == 3:
            doubler = 2
            print(self.player1.name, "just won using the same move for the fourth time in a row. That means the points scored this round are doubled!")
        else:
            doubler = 1
        
        if self.consec_wins >= 7:
            self.player1.score = self.player1.score + 3 * doubler
        elif self.consec_wins == 6:
            self.player1.score = self.player1.score + 2.5 * doubler
        elif self.consec_wins == 5:
            self.player1.score = self.player1.score + 2 * doubler
        elif self.consec_wins == 4:
            self.player1.score = self.player1.score + 1.8 * doubler
        elif self.consec_wins == 3:
            self.player1.score = self.player1.score + 1.5 * doubler
        elif self.consec_wins == 2:
            self.player1.score = self.player1.score + 1.2 * doubler
        else:
            self.player1.score = self.player1.score + 1 * doubler
        
        
    def p1_lose(self, p1_choice, p2_choice):
        print(self.player1.name, "'s ", p1_choice, " loses to ", self.player2.name, "'s ", p2_choice,sep = "")
        
        if self.last_winner == 2:
            self.consec_wins = self.consec_wins + 1
        else:
            self.last_winner = 2
            self.consec_wins = 1
        
        if self.player2.prev_same_moves == 3:
            doubler = 2
            print(self.player2.name, "just won using the same move for the fourth time in a row. That means the points scored this round are doubled!")
        else:
            doubler = 1
        
        if self.consec_wins >= 7:
            self.player2.score = self.player2.score + 3 * doubler
        elif self.consec_wins == 6:
            self.player2.score = self.player2.score + 2.5 * doubler
        elif self.consec_wins == 5:
            self.player2.score = self.player2.score + 2 * doubler
        elif self.consec_wins == 4:
            self.player2.score = self.player2.score + 1.8 * doubler
        elif self.consec_wins == 3:
            self.player2.score = self.player2.score + 1.5 * doubler
        elif self.consec_wins == 2:
            self.player2.score = self.player2.score + 1.2 * doubler
        else:
            self.player2.score = self.player2.score + 1 * doubler

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.m_current = "NA"
        
        # How many consecutive turns have had the same move
        # Resets to 1 evertime a new move is played
        # Adds one if same move from previous turn is played 
        self.prev_same_moves = 0
        
    def prompt_turn(self, reduced_choices):
        
        if reduced_choices:
            options = ["rock", "paper", "scissors"]
            options.remove(self.m_current)
            
            rng = random.random() < 0.5
            
            second_option = options[rng]
            
            print(self.name, " has had 3 or 6 consecutive wins, you can either play your previous move or a random selected one.")
            print(self.name, ", what would you like to play (", self.m_current, " or ", second_option, ")", sep = "")
            
            m_next = input()
            while m_next != self.m_current and self.m_current != second_option:
                print("You must choose from the choices (", self.m_current, " or ", second_option, ")", sep = "")
                m_next = input()
            
        else:
            print(self.name, "what would you like to play (rock, paper, or scissors)")
            m_next = input()
            while m_next != "rock" and m_next != "paper" and m_next != "scissors":
                print("You must choose from the choices (rock, paper, or scissors)")
                m_next = input()
        
        
        if self.m_current == m_next:
            self.prev_same_moves = self.prev_same_moves + 1
        else:
            self.prev_same_moves = 0
        
        self.m_current = m_next
        
        return(self.m_current)
        

p1 = input("What is Player 1's name? ")
p2 = input("What is Player 2's name? ")
rounds = input("How many rounds would you like to play? ")
try:
    rounds = int(rounds)
except ValueError:
    print("Rounds must be an integer")
    
print()

g1 = Game(Player(p1), Player(p2), rounds)

g1.start_game()


















