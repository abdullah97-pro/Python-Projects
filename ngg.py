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
        attempts_left = max_attempts - attempts

        # Get player's guess with input validation
        while True:
            try:
                guess = int(input(f"\nAttempt {attempts}/{max_attempts}. Enter your guess: "))
                # check if guess is withing valid rang 
                if guess < min_num or guess > max_num:
                    print(f"Please enter a number between {min_num} and {max_num}")
                else:
                    break
            except ValueError:
                print("Please enter a valid number!")

            # check the guess using comparison operators
            if guess == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempt(s)!")
                guessed_correctly = True
            elif guess < secret_number:
                print(f"Too low",end="")

                # Give hints based on how close the guess is 
                if secret_number - guess > 20:
                    print("Way too low.")
                elif secret_number - guess > 10:
                    print("Still quite low!")
                else:
                    print("Getting closer")
            else:
                print(f"Too high!", end="")

                # Give hints based on how close the guess is
                if guess - secret_number > 20:
                    print("Way too high!")
                elif guess - secret_number > 10:
                    print("Still quite high")
                else:
                    print("Getting close!")
            
            # show attempts left if not the last attempt
            if not guessed_correctly and attempts > 0:
                print(f"You have {attempts_left} attempt(s) remaining.")

        # Game over message
        print("\n" + "="*40)
        if guessed_correctly:
            print("YOU WIN! Well done!")

            # bonus
            score_percentage = int(((max_attempts - attempts + 1)/max_attempts)*100)
            print(f"Your score: {score_percentage}%")

            if score_percentage >= 80:
                print("Excellent performance!")
            elif score_percentage >= 60:
                print("Good job")
            else:
                print("You made it")
        else:
            print(f"GAME OVER! The number was {secret_number}")
            print("Best of luck next time!")
    
    #ask if player wants to play again
    play_again = input("\n Would you like to play again?(yes/no): ").lower()

    # using logical operator to check reponse
    if play_again == "yes" or play_again == "y":
        print("\n" + "="*40)
        number_guessing_game()
    else:
        print("\nThanks for playing!")
            
# start game
if __name__ == "__main__":
    number_guessing_game()