# Coin_toss-Game
# 💸 Coin Toss Simulator

A simple Python program that simulates flipping a coin, returning either **Head** or **Tail** randomly — now with added score tracking and a fun animation!

## 🎯 Features

- Simulates a fair coin toss using Python’s `random` module  
- Interactive command-line interface  
- ASCII animation of the coin flipping  
- Tracks total flips, Heads, and Tails count  
- Validates user input using `.strip().lower()`  

## 🛠 How It Works

The `coin_toss()` function uses `random.randint(0, 1)` to return `"Head"` or `"Tail"`. An ASCII-style flipping animation (`...`) is shown before displaying the result. The main loop continues until the user enters `"no"`.

User input is cleaned using `.strip().lower()` to handle extra spaces or capital letters.

The program tracks:
- Total number of flips
- Count of Heads
- Count of Tails

All stats are displayed when the user chooses to stop.


## 💡 Example Output
Do you want to play?
yes or no: Yes
Flipping the coin...
The side that landed is: Head

Do you want to play?
yes or no: maybe
Invalid input!! Enter yes or no in small alphabets

Do you want to play?
yes or no: no

Thanks for playing!
Total Tosses: 3
Heads: 2
Tails: 1
