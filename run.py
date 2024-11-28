# Import the random module to select a random word.
import random

# Import for terminal clearing.
import os

# Import for colored output.
from colorama import Fore, Style

WORD_BANK = ["python", "hangman", "game", "programming", "project", "developer"]
"""
Word bank for the game,
This list contains the words that our game will randomly choose from.
"""


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


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
    progress = []
    for letter in word:
        if letter in guessed_letters:
            progress.append(letter)
        else:
            progress.append("_")

    return " ".join(progress)
    # Join the list into a spaced string.


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
            print(f"You already guessed '{guess}'. ")
            # This is a repeated guess.
            return None
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
    clear()
    print("Welcome to Hangman!")
    print("Game is starting. Stay tuned!")

    chosen_word = choose_word()
    print(f"The chosen word (for testing): {chosen_word}\n")

    # Create an empty set of guessed letters
    guessed_letters = set()
    
    remaining_attempts = 6

    progress = display_progress(chosen_word, guessed_letters)

    # Display the initial progress(underscores).
    print(f"Word progress: {progress}")

    while True:
        clear()
        # Show remaining attempts
        print(f"Remaining attempts: {remaining_attempts}")

        # Get player's guess.
        player_guess = get_player_guess(guessed_letters)

        # If guess is a repeat show progress and skip processing.
        if player_guess is None:
            print(f"You already guessed that letter!")
            print(f"Word progress: {display_progress(chosen_word, guessed_letters)}")
            continue

        # Add the guess to the set of guest letters.
        guessed_letters.add(player_guess)

        # Check if the guess is in the chosen word.
        if player_guess in chosen_word:
            print(Fore.GREEN + f"Good guess! '{player_guess}' is in the word." + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Oh no! '{player_guess}' is not in the word." + Style.RESET_ALL)
            remaining_attempts -= 1

        # Update and display.
        progress = display_progress(chosen_word, guessed_letters)
        print(f"Word progress: {progress}")

        # Check for win condition.
        if "_" not in progress:
            print(Fore.YELLOW + f"Well done! you guessed the word: {chosen_word}" + Style.RESET_ALL)
            break
        # Check for lose condition.
        if remaining_attempts == 0:
            print(Fore.RED + f"Game Over! The word was: {chosen_word}" + Style.RESET_ALL)
            break


main()
