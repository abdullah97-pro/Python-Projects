import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("="*40)

    # Game Settings
    difficulty_levels = {
        "1": {"range":(1,10),"attempts":5,"name":"Easy (1-10)"},
        "2": {"range":(1,50),"attempts":7,"name":"Midum (1-50)"},
        "3": {"range":(1,100),"attempts":10,"name":"Hard (1-100)"}
    }

    # let player choose difficulty
    print("\n Choose your difficulty level:")
    for key, value in difficulty_levels.items():
        print(f"{key}, {value['name']} - {value['attempts']} attempts")

number_guessing_game()