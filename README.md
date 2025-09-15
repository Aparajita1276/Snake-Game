# 🐍 Modular Snake Game (Python + Turtle)

A classic Snake Game built in Python using the `turtle` graphics library — now written in a clean **modular structure** with separate files for the Snake, the Food, and the main game loop.


## 📁 Project Structure
snake.py- Snake class and movement logic  
food.py- Food class  
main game.py- Main game loop and scoring  


## 🎮 Features

- Smooth snake movement using `ontimer` (no infinite while loop).
- Food randomly appears, and the snake grows when it eats.
- Score and high score are displayed at the top.
- Collision detection with walls and self.
- Clean object-oriented, modular code (easy to maintain).


## 🛠 Requirements

- Python 3.8+  
- `turtle` module (built-in with Python)  


## 🚀 How to Run

1. Clone or download this repository.
2. Make sure `snake.py`, `food.py`, and `main.py` are in the same folder.
3. Run 
4. Use the arrow keys to control the snake


## 📚 Code Overview  

snake.py — Handles the snake’s body segments, movement, and direction changes.  
food.py — Handles the food object and random repositioning.  
main.py — Creates the window, scoreboard, connects everything, and runs the main game loop.  


## 🖥 Gameplay  

Eat the red food to grow and earn points.  
Avoid hitting the walls or your own tail.  
The game automatically resets when you lose.  


## ✨ Possible Enhancements  

Add sound effects when eating food or on game over.  
Add multiple levels with speed increases.  
Add a pause/resume feature.  
Add different food types with varying points.  
