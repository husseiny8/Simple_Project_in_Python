# Rock Paper Scissors Game

A simple command-line implementation of the classic Rock, Paper, Scissors game built with Python. The player competes against the computer, which makes random choices each round.

This project is ideal for beginners learning Python fundamentals such as functions, loops, conditionals, user input handling, and random number generation.

## Features

* Interactive command-line gameplay
* Random computer moves
* Win, lose, and draw detection
* Continuous play mode
* Quit option to exit the game
* Beginner-friendly code structure

## Technologies Used

* Python 3
* random module
* sys module

## Game Rules

The game follows the traditional rules:

| Player Choice | Beats    |
| ------------- | -------- |
| Rock          | Scissors |
| Paper         | Rock     |
| Scissors      | Paper    |

### Outcomes

* If both players choose the same option → Draw
* If your choice beats the computer's choice → You Win
* Otherwise → Computer Wins

## Project Structure

```text
rock-paper-scissors/
│
├── rock_paper_scissors.py
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/rock-paper-scissors.git
cd rock-paper-scissors
```

## Usage

Run the game:

```bash
python rock_paper_scissors.py
```

When prompted, enter one of:

```text
Rock
Paper
Scissors
```

Or type:

```text
Quit
```

to exit the game.

## Example Gameplay

```text
Rock, Paper, Scissors? Or Quit? Rock

PC Choice: Scissors
You win
```

Another example:

```text
Rock, Paper, Scissors? Or Quit? Paper

PC Choice: Paper
Draw
```

## How It Works

### User Input

The player is repeatedly prompted until a valid choice is entered.

```python
def user_input():
```

### Computer Choice

The computer randomly selects one of the available options.

```python
def computer_choice():
```

### Winner Determination

The game compares both choices and determines whether:

* The player wins
* The computer wins
* The round ends in a draw

```python
def determine_winner(user_choice, computer_choice):
```

### Main Game Loop

The game runs continuously until the user enters `Quit`.

```python
def main():
```

## Learning Objectives

This project helps beginners practice:

* Functions
* Conditional statements
* Infinite loops
* User input validation
* Random value generation
* Program termination with `sys.exit()`


## License

This project is open source and available under the MIT License.
