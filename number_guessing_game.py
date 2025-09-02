import random  # Import random module to generate random numbers

# Function to play the guessing game
def play_game():
    # Computer chooses a random number between 1 and 100
    number = random.randint(1, 100)
    attempts = 0  # To count how many guesses the player makes
    
    print("\nI have chosen a number between 1 and 100.")
    print("Try to guess it!\n")
    
    while True:
        try:
            # Take input from user
            guess = int(input("Enter your guess: "))
            attempts += 1  # Increase attempt count
            
            # Check the guess and give feedback
            if guess > number:
                print("Too High! Try again.")
            elif guess < number:
                print("Too Low! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.\n")
                break  # Exit loop when guessed correctly
        except ValueError:
            print(" Invalid input! Please enter a number between 1 and 100.")

# Main function to control the game loop
def main():
    print("===== Welcome to the Number Guessing Game =====")
    
    while True:
        # Start a new game
        play_game()
        
        # Ask player if they want to play again
        choice = input("Do you want to play again? (yes/no): ").lower()
        
        if choice != "yes":
            print("👋 Thanks for playing! Goodbye.")
            break  # Exit the loop to end the game

# Run the main function
if __name__ == "__main__":
    main()