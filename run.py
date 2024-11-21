"""
Import the random module to select a random word
"""
import random

"""
Word bank for the game,
This list contains the words that our game will randomly choose from.
"""
WORD_BANK = ["python", "hangman", "game", "programming", "project", "developer"]

def choose_word():
    """
    Randomly choose a word from the word bank.
    """
    return random.choice(WORD_BANK)

def display_progress(word, guessed_letters):
    """
    Replace letters in the word that have not been guessed with underscores.
    Guessed letters are revealed in their correct position.
    Unguessed letters are shown as "_".
    """
    progress = [letter if letter in guessed_letters else "_" for letter in word]
    """
    For each letter in the word, show it if guessed, otherwise show "_".
    """
    return " ".join(progress)
    """
    Join the list into a spaced string.
    """

def get_player_guess(guessed_letters):
    """
    Function to get a valid letter guess from the player.
    """

    while True:
        guess = input("Enter a letter (or type 'exit' to quit): ").lower().strip()

        # Check if the player wants to exit/quit.
        if guess == "exit":
            print("Thanks for playing!")
            exit()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter!")
        else:
            return guess
    """
    Ask the player for a letter and validate the input.
    Ensure it's a single letter.
    Ensure the letter hasn't been guessed already.
    """

def main():
    """
    Main function to run the Hangman game.
    """
    print("Welcome to Hangman!")
    print("Game is starting. Stay tuned!")

    chosen_word = choose_word()
    print(f"The chosen word (for testing): {chosen_word}\n")
    
    guessed_letters = set()
    """
    Create an empty set of guessed letters
    """
    
    progress = display_progress(chosen_word, guessed_letters)
    print(f"Word progress: {progress}")
    """
    Display the initial word progress(underscores).
    """

    while True:
        # Get player's guess.
        player_guess = get_player_guess(guessed_letters)

        # Add the guess to the set of guest letters.
        guessed_letters.add(player_guess)

        # Update and display.
        progress = display_progress(chosen_word, guessed_letters)
        print(f"Word progress: {progress}")
    

main()