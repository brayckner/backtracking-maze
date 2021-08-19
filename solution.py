# Brayckner
# 08/18/2021


#  BackTracking Problem
maze = [[" . ", " . ", " . ", " . ",],
        [" x ", " x ", " x ", " . ",],
        [" . ", " . ", " . ", " . ",],
        [" x ", " x ", " . ", " . ",]]

def printMaze(maze):
    for row in maze:
        rowPrint = ""
        for value in row:
            rowPrint += value + " "
        print(rowPrint)

printMaze(maze)

def solveMaze(maze):
    if len(maze) < 1:
        return None 
    if len(maze[0]) < 1:
        return None 
    return solveMazeHelper(maze, [ ], 0, 0)
    
def solveMazeHelper(maze, sol, posRow, posCol):
    # Get Size of the Maze
    numRow = len(maze)
    numCol = len(maze[0])

    # Base Cases ==============================

    # Robot is already home
    if posRow == numRow -1 and posCol == numCol:
        return sol
    
    # Out of bounds
    if posRow >= numRow or posCol >= numCol:
        return None 

    # Is on an obstacle
    if maze[posRow][posCol] == 'x':
        return None 

    # Recursive Cases ==============================

    # Try going right
    sol.append("r")
    solGoingRight = solveMazeHelper(maze, sol, posRow, posCol + 1)
    if solGoingRight is not None:
        return solGoingRight
    
    # Going right doesn't work, Backtrack, trying going down
    sol.pop()
    sol.append("d")
    solGoingDown = solveMazeHelper(maze, sol, posRow + 1, posCol)
    if solGoingDown is not None:
        return solGoingDown

    # No solution, impossible, Backtrack
    sol.pop()
    return None

print(solveMaze(maze))