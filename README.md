# connect4project

Connect 4 is a classic strategy game where players take turns dropping colored discs into a grid with the goal of connecting four of their own discs in a row, either horizontally, vertically, or diagonally. It's a simple yet challenging game that requires strategic thinking and planning ahead.

<p align="center">
<img src="/previews/Screenshot_menu.png" width="30%"/>
<img src="/previews/Screenshot_ingame.png" width="30%"/>
<img src="/previews/Screenshot_final.png" width="30%"/>
</p>

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Installation

Install required libraries. Only required library is Pygame for now.

```python
pip install pygame
```

## Usage

### Gameplay

- Click to blanks under 'Red Player' and 'Black Player' in the menu and fill.
- Click the "Start" button to begin.
- Click on a column to place a disc.
- Win the game by connecting four discs in a row horizontally, vertically, or diagonally.

### Continue Previous Game

- If a previous game is closed before win condition met, click the "Continue" button in the menu.

### Exiting the Game

- Close the game window to exit.

## Features

**Connect 4 Gameplay**: Experience the classic Connect 4 gameplay, where players aim to connect four discs of their own color.

**Data Persistence**: The game stores the current state of the game, including last player, current player, usernames and game progress, using JSON serialization in a text file.


