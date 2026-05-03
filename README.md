# Number Guessing Game 🎮

A simple Python game where the computer randomly selects a number between 1 and 100, and the player tries to guess it.

---

## 📌 Features

- Random number generation
- User input handling
- “Too High” and “Too Low” hints
- Attempt counter
- Score calculation
- Beginner-friendly Python project

---

## 🛠 Technologies Used

- Python
- `random` module

---

## 📂 How the Game Works

1. Computer generates a random number between 1 and 100.
2. Player enters a guess.
3. Program checks:
   - If guess is higher → shows `📈 Too High`
   - If guess is lower → shows `📉 Too Low`
   - If correct → player wins
4. Total attempts are counted.
5. Final score is displayed.

---

## ▶️ How to Run

### Step 1: Save the file

Save the code as:

```bash
number_guessing_game.py
```

### Step 2: Run the program

```bash
python number_guessing_game.py
```

---

## 💻 Python Code

```python
import random

# Computer chooses random number
secret_number = random.randint(1, 100)

attempts = 0

print("🎮 Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))

    attempts += 1

    if guess > secret_number:
        print("📈 Too High!")

    elif guess < secret_number:
        print("📉 Too Low!")

    else:
        print("🎉 Correct Guess!")
        print(f"You guessed the number in {attempts} attempts.")

        # Score Calculation
        score = 100 - attempts

        if score < 0:
            score = 0

        print(f"🏆 Your Score: {score}")

        break
```

---

## 💻 Example Output

```text
🎮 Welcome to Number Guessing Game!
Guess a number between 1 and 100

Enter your guess: 40
📉 Too Low!

Enter your guess: 80
📈 Too High!

Enter your guess: 65
🎉 Correct Guess!

You guessed the number in 3 attempts.
🏆 Your Score: 97
```

---

## 🧠 Concepts Used

- Variables
- Loops
- Conditional Statements
- User Input
- Random Numbers

---

## 🚀 Future Improvements

- Difficulty Levels (Easy / Medium / Hard)
- Limited attempts
- Multiplayer mode
- Timer feature
- High score system
- GUI using Tkinter or Pygame

---

## 📚 Learning Outcome

This project helps beginners practice:
- Problem solving
- Game logic
- Python fundamentals
- User interaction

---

## 👨‍💻 Author

Created by Bhavan Sandeep Patil.
