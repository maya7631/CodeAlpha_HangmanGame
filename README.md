# Hangman Game

**Student Name:** Mayank Kumar  
**Internship:** CodeAlpha – Python Programming  
**Task:** Task 1 – Hangman Game

## Project Description
A simple text-based Hangman game written in Python. The computer selects one word randomly from a predefined list of five words. The player guesses the word one letter at a time.

## Requirements Covered
- Uses a small list of **5 predefined words**.
- Allows a maximum of **6 incorrect guesses**.
- Uses basic console input and output.
- Uses Python's `random` module, loops, conditional statements, strings, and lists.
- No graphics, audio, external packages, files, or APIs are required.

## How to Run
1. Install Python 3.
2. Open this folder in VS Code.
3. Open the integrated terminal (**Terminal → New Terminal**).
4. Run:

   ```bash
   python hangman.py
   ```

   On some Windows installations, use:

   ```bash
   py hangman.py
   ```

## How to Play
- Enter one alphabet letter when prompted.
- Correct guesses reveal the matching letters.
- Incorrect guesses increase the incorrect-guess count.
- The game ends when the word is guessed or 6 incorrect guesses are made.

## Testing Checklist
- [ ] Correct letter reveals it in the word.
- [ ] Incorrect letter increases the incorrect-guess count.
- [ ] Repeated letter is not counted again.
- [ ] Blank input, numbers, and multiple characters are rejected.
- [ ] Game ends after 6 incorrect guesses.
- [ ] Game reports a win when all letters are guessed.

## Files
- `hangman.py` – main game program.
- `.gitignore` – ignores Python cache and local editor files.

## Student Note
Review the code, run it yourself, and make sure you can explain the game loop, random word selection, input validation, and win/lose conditions before submitting.
