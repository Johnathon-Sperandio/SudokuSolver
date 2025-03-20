***\*WARNING: DEVELOPEMENT IN PROGRESS; INFORMATION SUBJECT TO CHANGE\****
________________________________________________
# SudokuSolver v0.0

### This is an automatic Sodoku Solver that utilizes backtracking and number storage to efficiently solve Sudoku puzzles

* This is not intended to be an optimized project, it is just for me to relearn the basics of coding in a fun way!
* I will do this project in python first, I may redo it in other languages later.

________________________________________________
# Basic Info

## Structure:

* The board will be a classic layout of {letter, number}, wherein the letter represents the row and the number represents the column:

|    |    |    |    |    |    |    |    |    |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **A1** | **A2** | **A3** | *A4* | *A5* | *A6* | **A7** | **A8** | **A9** |
| **B1** | **B2** | **B3** | *B4* | *B5* | *B6* | **B7** | **B8** | **B9** |
| **C1** | **C2** | **C3** | *C4* | *C5* | *C6* | **C7** | **C8** | **C9** |
| *D1* | *D2* | *D3* | **D4** | **D5** | **D6** | *D7* | *D8* | *D9* |
| *E1* | *E2* | *E3* | **E4** | **E5** | **E6** | *E7* | *E8* | *E9* |
| *F1* | *F2* | *F3* | **F4** | **F5** | **F6** | *F7* | *F8* | *F9* |
| **G1** | **G2** | **G3** | *G4* | *G5* | *G6* | **G7** | **G8** | **G9** |
| **H1** | **H2** | **H3** | *H4* | *H5* | *H6* | **H7** | **H8** | **H9** |
| **I1** | **I2** | **I3** | *I4* | *I5* | *I6* | **I7** | **I8** | **I9** |

There following sub-structures will be kept track of for use in the code:

1. Each Row (9) (groups denoted by alphabet)
2. Each Column (9) (groups denoted by number)
3. Each Group of 9 blocks (Grid) in the puzzle (9)
    1. The grids are noted by grouping the **bold** and *italicized* blocks.

## Classes:

Each individual square will hold a set of numbers. This set will either start out with one number or all the numbers:
1. *Set of a Single Number*
    1. Assigned at start according to puzzle.
2. *Set of All the Numbers*
    1. Full of all numbers 1-9 at start.
    2. Each number is a potential candidate to be the last number remaining.

Each individual square must keep track of it's own state between the following states:
1. **Concrete** (number was assigned at start of game, should be a correct state)
2. **Prospective** (an initially full set of numbers that will be emptied until one number remains)
3. **Set** (only one number that can go in this spot according to Sudoku rules remains)

## Algrithm Flow:

After receiving an unsolved board, first the structures will be updated with the proper concrete numbers and the prospective sets will be filled with all numbers.

Starting from the top left, each individual square will be examined one at a time. If the square is **Concrete** or **Set**, then the algorithm will do *three* things:
1. Remove that number from the rest of the column.
2. Remove that number from the rest of the row.
3. Remove that number from the rest of the grid group.
- Anytime a number is removed from a square, a check is made to make sure to update state if only one number is left.

After these actions occur, the algorithm moves on to the next square.

If the square is **Prospective**, the algorithm moves on to the next square.

This is version 0, so this may only solve the most basic puzzles.

## Functions:

bool board_init(string board):

* Intakes unsolved board into string **board**.
* Assigns Structure and Classes data as needed according to **board**.
* *returns*: true if success, false if error.

bool set_square(stuct **square**):

* Changes **square** state to **Set**.
* Increments *Count*.
* *returns* true if success, false if error.

bool examine_square(struct **square**):

* Intakes **square** to be examined.
* Calls other functions according to actions required by Algorithm Flow.
* *returns*: true if success, false if error.

bool remove_from_row(struct **struct**, int **number**):

* Intakes **struct** (row, column, or grid) that it is called from and **number** of the number to remove.
* iterates through struct, removing number if state is **Prospective** and number is there.
* *returns* true if success, false if error.

## Variables:

int *Count*:

* Set to zero at init, incremented for each cement and set number, if 81 is reached, all squares are either cement or set, thus the puzzle is solved.