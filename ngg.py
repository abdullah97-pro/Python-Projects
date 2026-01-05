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
    
    while True:
        choice = input("\nEnter your choice (1-3):")

        # check if choice is valid 
        if choice in ["1","2","3"]:
            min_num, max_num = difficulty_levels[choice]["range"]
            max_attempts = difficulty_levels[choice]["attempts"]
            difficulty_name = difficulty_levels[choice]["name"]
            break
        else:
            print("Invalid choice! Please enter 1,2,3")

    # Generate random number
    secret_number = random.randint(min_num,max_num)

    print(f"\nI'm thinking of a number between {min_num} and {max_num}")
    print(f"You have {max_attempts} attempts to guess it.")
    print("-"*40)

    # Game loop
    attempts = 0
    guessed_correctly = False

    while attempts < max_attempts and not guessed_correctly:
        attempts += 1

number_guessing_game()