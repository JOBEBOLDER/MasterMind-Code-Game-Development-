# 🎯 Mastermind Game (Python Turtle Edition)

This repository contains a **Python Turtle-based Mastermind Game**, designed and implemented using a modular and layered approach.

## 🧠 Overview

Mastermind is a classic code-breaking game. In this version, players try to guess a secret color code by interacting with a graphical interface built using the `turtle` module. The game provides real-time visual feedback, score tracking, and a leaderboard system.

---

## 🗂️ Project Structure

Here's a brief description of the key files and directories:

```
📁 Mastermind_Starter_code/       # Starter templates and assets
📁 mastermind12.30/pythonProject2 # Main project code
├── 11.22.py                      # Additional gameplay feature
├── Marble.py                     # Game piece logic (marble drawing, etc.)
├── Point.py                      # Score system
├── coco.py, coco11.25.py         # Color and logic variations
├── game_board_principle_coco.py  # Board layout and logic concept
├── plan.py, lecture10.py         # Planning or lecture reference files 
├── Main.py                       # 🔥 GameMain class – entry point
├── mastermind_errors.txt         # Known issues or debugging notes
├── mastermind12.30.zip           # Packaged version of the game
├── *.gif                         # UI image assets (buttons, win/lose screens)
├── leaderboard.txt               # Leaderboard data
```

---

## 📦 Main Components

### 1. `GameUi` Class – User Interface

Handles the visual representation of the game using Python's `turtle` library.

#### Key Responsibilities:
- Displaying the game board and score panel
- Showing color selections and player input
- Showing win/lose feedback and arrows
- Handling button interactions (confirm, delete, quit)

---

### 2. `GameFunction` Class – Game Logic

Manages the core logic of the game including color matching and score tracking.

#### Key Methods:
- `secret_code()`: Randomly creates the answer
- `fill_color()`: Records user guesses
- `confirm_answer()`: Checks guess accuracy
- `delete_answer()`: Clears last input
- `write_leaderboard()` / `load_leaderboard()`: Handles persistent scores

---

### 3. `GameMain` Class – Game Execution

Acts as the control center, connecting UI and logic modules together.

#### Key Features:
- Initializes the game environment and turtle screen
- Handles click events and user interactions
- Tracks round number, game state, and player progress

---

## 🚀 How to Run

1. Clone this repository
2. Make sure you have Python 3.x installed
3. Run the `Main.py` file:

```bash
python Main.py
```

4. Enjoy the game! You'll be prompted to enter your name and start playing.

## 🧩 Features

- 🎨 Intuitive turtle graphics UI
- 🔄 Real-time color feedback
- 🏆 Leaderboard support
- ❌ Delete last guess feature
- ✅ Confirm and validate guesses
- 🧠 Modular code structure (UI, Logic, Execution separated)

## 🛠️ Requirements

- Python 3.x
- No external libraries are needed. Everything runs with the built-in turtle and random modules.

## 📌 Credits

This project was created as part of a programming course assignment. Special thanks to all contributors and reviewers who helped test and improve the game logic and UI.

## 📝 Note

The folder includes .gif image assets used by the turtle UI, along with some helper Python files and zipped packages. If running locally, please ensure all paths are correct and images are available in the expected directory.

---

Enjoy playing and learning with this visual, interactive Python game!
<img width="821" alt="image" src="https://github.com/user-attachments/assets/c17040a2-3edd-472a-a6f2-cef21271ce58" />
<img width="858" alt="image" src="https://github.com/user-attachments/assets/5077b9df-4eed-4701-8aa2-b816df474fc7" />

