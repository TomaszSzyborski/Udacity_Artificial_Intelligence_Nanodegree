# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: The Naked twins problem states that none of the boxes in the units that contain both of the naked twins boxes in exception for two boxes can contain the twin values.

By eliminating these twin values from the digit possibilities of the non-naked twin boxes, sudoku simpler to solve as there is less possibilities to choose a number for given boxes - local constraint was used to reduce the search space. As a result enforcing constraints in other boxes/units that were previously unidentifiable, it made possible to solve the puzzle by tkaing algorithm steps closer to having one digit per box - which was not possible to achieve such result using only _eliminate_ or _only-choice_

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: There should be only two new constraints added - regarding diagonal units. It has to be coded (as adding new units) in _unitlist_ variable.
The rules of the constraints are the same as previous (only 1 copy of a digit 1 to 9 is allowed in the unit), so simple addition (of aforementioned units) to the unit lists is sufficient. The strategies: elimination, only_choice, naked_twins stay the same, but complexity rises as there is more units to check and more peers, however the search space can be reduced as certain choices (e.g. on diagonals) can be omitted right away.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the `assign_value` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login) for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.

