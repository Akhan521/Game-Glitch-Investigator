# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

It appeared to look like a normal number guessing game, but the hints were not correct. The text on the screen was also problematic, in the sense that toggling between different modes didn't update the text as expected. I also noticed that the new game button didn't work as intended, as it didn't reset the game nor the hints properly.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  I felt as thought the hints were not accurate; possibly, they could be flipped. For example, the secret was 57, yet any number below 57 caused the hint to say "Go lower". I also noticed that the text on the screen didn't update when I toggled between different modes, which was confusing. A third bug I noticed was that the new game button didn't truly reset the game (hints were not reset properly). I'm certain there are more bugs, but these were the first ones that I noticed when I ran the game for the first time.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude Code as my primary AI tool for this project. I found it to be extremely helpful in refactoring our project's code and addressing the bugs we encountered. I didn't use any other AI tools for this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One example of a correct AI suggestion was when I asked Claude Code to refactor the game logic out of app.py into logic_utils.py. Claude Code suggested a clear way to separate the game logic from the Streamlit app code, which cleanly organized game logic in logic_utils.py and UI code in app.py. I verified the result by running the game after the refactor and confirming that everything still worked as expected. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

One example of an incorrect AI suggestion was when I asked Claude Code to fix the issue of resetting the game state. Claude Code suggested a solution in which we reset attempts to 1 instead of 0 when starting a new game. This was incorrect because it caused the attempts count to be off by one, leading to an inaccurate display of attempts left. I verified the result by running the game and noticing that the attempts count was always one less than it should be. I corrected it by changing the reset value to 0, to show the correct number of attempts left when starting a new game.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
