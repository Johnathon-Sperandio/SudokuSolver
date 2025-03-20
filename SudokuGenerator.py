# Sudoku Generator generated utilizing ChatGPT4o
# https://chatgpt.com/share/67db9a8e-7ea8-8013-8d0b-e25ba270a7ee 
from sudoku import Sudoku
import json

def generate_sudoku(difficulty=0.5):
    """
    Generate a Sudoku puzzle with the given difficulty.
    Difficulty ranges from 0 (easy) to 1 (hard) not inclusive.
    """
    puzzle = Sudoku(3).difficulty(difficulty)
    return puzzle.board

def save_puzzle(puzzle, filename="sudoku_puzzle.json"):
    with open(filename, "w") as f:
        json.dump(puzzle, f)
    print(f"Puzzle saved to {filename}")

if __name__ == "__main__":
    difficulty = float(input("Enter difficulty (0.0 to 1.0): "))
    puzzle = generate_sudoku(difficulty)
    save_puzzle(puzzle)
    
    print("Generated Sudoku Puzzle:")
    for row in puzzle:
        print(row)
