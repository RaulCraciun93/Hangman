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

def main():
    """
    Main function to run the Hangman game.
    """
    print("Welcome to Hangman!")
    print("Game is starting. Stay tuned!")

    chosen_word = choose_word()
    print(f"The chosen word (for testing): {chosen_word}\n")

main()