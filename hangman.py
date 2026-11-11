import random

# Five predefined words, as required by the CodeAlpha task.
WORDS = ["python", "gaming", "satellite", "cricket", "computer"]
MAX_WRONG_GUESSES = 6


def show_word(secret_word, guessed_letters):
    """Return the word with unguessed letters hidden."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def play_game():
    secret_word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0

    print("\n================================")
    print("          HANGMAN GAME")
    print("================================")
    print("Guess the hidden word, one letter at a time.")
    print(f"You can make up to {MAX_WRONG_GUESSES} incorrect guesses.")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("\nWord:", show_word(secret_word, guessed_letters))
        print("Incorrect guesses:", wrong_guesses, "/", MAX_WRONG_GUESSES)

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word!")
            return

        guess = input("Enter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Incorrect guess!")

    print("\nGame over! You used all 6 incorrect guesses.")
    print("The correct word was:", secret_word)


if __name__ == "__main__":
    play_game()
