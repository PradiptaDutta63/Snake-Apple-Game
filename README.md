# Snake and Apple Game

## Project Overview
This project is a classic **Snake and Apple Game** built using Python's `pygame` library. The game involves controlling a snake to eat apples that randomly appear on the screen. As the snake eats apples, it grows longer, and the score increases. The game ends when the snake collides with itself. 

The project demonstrates skills in game development, graphics rendering, event handling, and collision detection.

---

## Features
1. **Snake Movement**:
   - Controlled by arrow keys.
   - Wraps around screen edges if it moves out of bounds.

2. **Apple Mechanics**:
   - Randomly spawns on the screen.
   - Increases the snake’s length when eaten.

3. **Game Over Screen**:
   - Displays the player's final score.
   - Offers an option to restart the game by pressing `ENTER`.

4. **Scoring System**:
   - Score is displayed dynamically during gameplay.

5. **Background Music and Sound Effects**:
   - Background music plays during the game.
   - Sound effects for eating an apple or colliding.

## Installation and Setup
**Prerequisites**
- Python 3.x
- `pygame` library

**Installation**
   1. Clone the repository:

```bash
git clone https://github.com/pradiptadutta63/snake-and-apple-game.git
cd snake-and-apple-game
```
   2. Install the dependencies:**

```bash
pip install -r requirements.txt
```
   3. Ensure all asset files are located in the resources/ folder.

**Running the Game**
   Run the game using:

```bash
python main.py
```

**How to Play**
   1. Use the arrow keys to move the snake:
      - `UP`, `DOWN`, `LEFT`, `RIGHT`.
   2. Eat apples to grow the snake and increase your score.
   3. Avoid colliding with yourself to keep the game running.
   4. If the game ends:
      - Press `ENTER` to restart.
      - Press `ESCAPE` to quit.

## Results and Features in Action
   - **Real-Time Scoring:** The player's score updates as apples are eaten.
   - **Game Reset:** After a collision, the game resets on pressing ENTER.
   - **Edge Wrapping:** The snake reappears on the opposite side of the screen if it exits the boundary.
   - **Dynamic Gameplay:** Random apple positioning keeps the game unpredictable and engaging.

## Contributors
Pradipta Dutta - Data Scientist 
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pradiptadutta63)