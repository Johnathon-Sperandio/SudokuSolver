# SudokuSolver

### This is an automatic Sodoku Solver that utilizes backtracking and number storage to efficiently solve Sudoku puzzles

* This is not intended to be an optimized project, it is just for me to relearn the basics of coding in a fun way!
* I will do this project in python first, I may redo it in other languages later.

________________________________________________

## Structure:

* The board will be a classic layout of {letter, number}, wherein the letter represents the row and the number represents the column:

| col 1 | col 2 | col 3 | col 4 | col 5 | col 6 | col 7 | col 8 | col 9 |
| ____ | ____ | ___ | ____ | ____ | ____ | _____ | ____ | ____ |
| A1 | A2 | A3 || A4 | A5 | A6 || A7 | A8 | A9 |
| B1 | B2 | B3 || B4 | B5 | B6 || B7 | B8 | B9 |
| C1 | C2 | C3 || C4 | C5 | C6 || C7 | C8 | C9 |
|______________________________________________|
| A1 | A2 | A3 || A4 | A5 | A6 || A7 | A8 | A9 |
| B1 | B2 | B3 || B4 | B5 | B6 || B7 | B8 | B9 |
| C1 | C2 | C3 || C4 | C5 | C6 || C7 | C8 | C9 |
|______________________________________________|
| A1 | A2 | A3 || A4 | A5 | A6 || A7 | A8 | A9 |
| B1 | B2 | B3 || B4 | B5 | B6 || B7 | B8 | B9 |
| C1 | C2 | C3 || C4 | C5 | C6 || C7 | C8 | C9 |
|______________________________________________|

