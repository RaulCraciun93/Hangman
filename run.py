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

def main():
    """
    Main function to run the Hangman game.
    """
    print("Welcome to Hangman!")
    print("Game is starting. Stay tuned!")

    chosen_word = choose_word()
    print(f"The chosen word (for testing): {chosen_word}\n")

    """
    Create an empty set of guessed letters
    """
    guessed_letters = set()

    """
    Display the initial word progress(underscores).
    """
    progress = display_progress(chosen_word, guessed_letters)
    print(f"Word progress: {progress}")

main()