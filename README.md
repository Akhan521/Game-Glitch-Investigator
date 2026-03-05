# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

Game's Purpose: To investigate and fix bugs in a Streamlit number guessing game, while reflecting on the debugging and AI-assisted development process.

Bugs Fixed:
- The hints were incorrect (e.g., "Go lower" when the guess was actually too low).
- Reset logic for the game state was flawed (e.g., status, score, history were not properly reset on new game).
- Changing difficulty mid-game did not update the secret number range or reset the game state.
- The attempts count was off by one due to incorrect reset value.
- Of course, there are likely more bugs that I haven't tackled yet, but these were the main ones I focused on fixing.

Fixes Applied:
- Refactored the code to separate game logic into `logic_utils.py` for better organization and maintainability.
- Updated the hint logic to correctly reflect whether the guess is too low, too high, or correct.
- Implemented proper reset logic to ensure that all relevant session state variables (status, score, history) are reset when starting a new game.
- Made the secret number range dynamic based on the selected difficulty level, and ensured that changing difficulty mid-game resets the game state appropriately.
- Corrected the reset value for attempts to 0 instead of 1 to accurately reflect the number of attempts left when starting a new game.

## 📸 Demo

<img width="1919" height="911" alt="winning_game" src="https://github.com/user-attachments/assets/99b569ec-f201-4661-bc3c-41d31c1006ec" />


