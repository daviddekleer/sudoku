# Sudoku

A sudoku solver written in Python. For each sudoku cell, the algorithm
determines the allowed numbers, loop through them and place them in the
puzzle. This process will be repeated recursively.

Each series of number placements is a branch in the search tree, if there
are no allowed numbers left the algorithm gives up this part of the tree
and backtracks to a previous part. The wrong numbers will be deleted from
the puzzle.

You can call `sudoku_solver` in `sudoku.py` with a 2D list like
```
[[8, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 3, 6, 0, 0, 0, 0, 0],
 [0, 7, 0, 0, 9, 0, 2, 0, 0],
 [0, 5, 0, 0, 0, 7, 0, 0, 0],
 [0, 0, 0, 0, 4, 5, 7, 0, 0],
 [0, 0, 0, 1, 0, 0, 0, 3, 0],
 [0, 0, 1, 0, 0, 0, 0, 6, 8],
 [0, 0, 8, 5, 0, 0, 0, 1, 0],
 [0, 9, 0, 0, 0, 0, 4, 0, 0]]
```

### Future additions
An interface visualizing the backtracking would be nice. I still have one
lying around somewhere from an earlier failed attempt to write a sudoku solver.

### Discussion
To admit, it's quite hard to follow what happens exactly during the
backtracking to me, so I need to analyze this a bit more. Finding the
current backtracking approach was also a bit of trial-and-error and intuition.