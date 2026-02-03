# 🎯 Number Guessing Game (CLI)

An interactive **command-line Number Guessing Game** built with Python. The game challenges users to guess a randomly generated number within a limited number of attempts, based on the selected difficulty level.

This project is designed to demonstrate **core Python skills**, clean control flow, input validation, and user-friendly CLI interaction.

---

## 🚀 Features

* 🎚️ **Difficulty Levels**

  * Easy: 1–50 (10 attempts)
  * Medium: 1–100 (7 attempts)
  * Hard: 1–200 (5 attempts)

* 🔁 **Replay Option** – Play multiple rounds without restarting the program

* ❌ **Input Validation** – Prevents crashes on invalid input

* 📉 **Attempt Tracking** – Shows remaining attempts after each guess

* 🧠 **Hints** – Tells whether the guess is too high or too low

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Concepts Used:**

  * Functions
  * Loops (`while`)
  * Conditional statements
  * Exception handling (`try-except`)
  * Random number generation

---

## 📂 Project Structure

```
number_guessing_game.py
README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed
2. Clone the repository or download the file
3. Run the program:

```bash
python number_guessing_game.py
```

---

## 🧩 How the Game Works

1. User selects a difficulty level
2. A random number is generated within the selected range
3. User guesses the number
4. The program provides hints (Too high / Too low)
5. Game ends when:

   * The user guesses correctly 🎉
   * Attempts run out ❌
6. User can choose to replay

---

## 📸 Sample Output

```
Select Difficulty Level:
1. Easy (1–50, 10 attempts)
2. Medium (1–100, 7 attempts)
3. Hard (1–200, 5 attempts)
Enter your choice: 2

Enter the number: 45
Too low
Attempts left: 6
...
Congratulations! You won the game 🎉
```

---

## 🌱 Learning Outcomes

* Writing clean, readable Python code
* Handling user input safely
* Structuring programs using functions
* Building interactive CLI applications

---

## 🔮 Future Improvements

* Score system or leaderboard
* Timer-based challenges
* OOP (class-based) implementation
* Unit tests

---

## 👩‍💻 Author

💌**Nandini Sharma**

---
