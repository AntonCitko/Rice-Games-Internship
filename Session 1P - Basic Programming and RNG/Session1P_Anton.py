import random

alive = True
user_lives = 5
turns_alive = 0

# Game continues to play until user runs out of lives
while user_lives > 0:
    
    turns_alive = turns_alive + 1
    
    # User input
    user_choice = input("Which way would you like to go (\"L\" for left or \"R\" for right): ")
    while user_choice != "L" and user_choice != "R":
        user_choice = input("Invalid choice. Which way would you like to go (\"L\" for left or \"R\" for right): ")
    
    # Convert to bool to compare to monster_choice
    user_choice = user_choice == "L"
    
    # Monster choice 50% chance of left or right
    monster_choice = random.random() < 0.5
    
    if monster_choice:
        print("The monster went left.")
    else:
        print("The monster went right.")
    
    # If, they have the same choice, no lives lost. Else, user loses life
    if monster_choice == user_choice:
        print("Congratulations you did not lose a life.")
    else:
        user_lives = user_lives - 1
        print("You lost a life. You have", user_lives, "more lives.")
    
    print("You have survived", turns_alive, "turns alive.")

print("You lost all your lives.")

if turns_alive < 6:
    score = "F"
elif turns_alive >= 6 and turns_alive < 10:
    score = "D"
elif turns_alive >= 10 and turns_alive < 12:
    score = "C"
elif turns_alive >= 12 and turns_alive < 15:
    score = "B"
elif turns_alive >= 15 and turns_alive < 20:
    score = "A"
else:
    score = "S"
    
print("You survived ", turns_alive, ". That means you scored an ", score, ". Great job!", sep = "")
