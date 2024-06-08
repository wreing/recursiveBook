
MAZE = """
#######################################################################
#S#                 #       # #   #     #         #     #   #         #
# ##### ######### # ### ### # # # # ### # # ##### # ### # # ##### # ###
# #   #     #     #     #   # # #   # #   # #       # # # #     # #   #
# # # ##### # ########### ### # ##### ##### ######### # # ##### ### # #
#   #     # # #     #   #   #   #         #       #   #   #   #   # # #
######### # # # ##### # ### # ########### ####### # # ##### ##### ### #
#       # # # #     # #     # #   #   #   #     # # #   #         #   #
# # ##### # # ### # # ####### # # # # # # # ##### ### ### ######### # #
# # #   # # #   # # #     #     #   #   #   #   #   #     #         # #
### # # # # ### # # ##### ####### ########### # ### # ##### ##### ### #
#   # #   # #   # #     #   #     #       #   #     # #     #     #   #
# ### ####### ##### ### ### ####### ##### # ######### ### ### ##### ###
#   #         #     #     #       #   # #   # #     #   # #   # #   # #
### ########### # ####### ####### ### # ##### # # ##### # # ### # ### #
#   #   #       # #     #   #   #     #       # # #     # # #   # #   #
# ### # # ####### # ### ##### # ####### ### ### # # ####### # # # ### #
#     #         #     #       #           #     #           # #      E#
#######################################################################
""".split('\n')

#Constants
EMPTY = ' '
START = 'S'
EXIT  = 'E'
PATH  = '.'

HEIGHT = len(MAZE)
WIDTH  = 0
for row in MAZE:
    if len(row) > WIDTH:
        WIDTH = len(row)

for i in range(len(MAZE)):
    MAZE[i] = list(MAZE[i])
    if len(MAZE[i]) != WIDTH:
        MAZE[i] =[EMPTY] * WIDTH


def printMaze(maze):
    
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(maze[y][x], end='')
        print()
    print()


def findStart(maze):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if maze[y][x] == START:
                return x,y

def solveMaze(maze, x=None, y=None, visited=None):
    if x==None or y==None:
        x,y = findStart(maze)
        print('Start = ', x, y)
    if visited == None:
        visited = []
    if maze[y][x] == EXIT:
        return True

    maze[y][x] = PATH
    visited.append(str(x) + ',' + str(y))
    printMaze(maze)

    print(x,y)
    #Explore the Neighboring Points
    #North
    if y+1 < HEIGHT and maze[y+1][x] in( EMPTY, EXIT) and str(x) + ',' + str(y+1) not in visited :
        if solveMaze(maze, x, y+1, visited):
            return True
    #South
    if y-1 >= 0 and maze[y-1][x] in( EMPTY, EXIT) and str(x) + ',' + str(y-1) not in visited :
        if solveMaze(maze, x, y-1, visited):
            return True
    #East
    if x+1 < WIDTH and maze[y][x+1] in( EMPTY, EXIT) and str(x+1) + ',' + str(y) not in visited :
        if solveMaze(maze, x+1, y, visited):
            return True
    #West
    if x-1 >= 0 and maze[y][x-1] in( EMPTY, EXIT) and str(x-1) + ',' + str(y) not in visited :
        if solveMaze(maze, x-1, y, visited):
            return True

    maze[y][x] = EMPTY #reset the empty space
    #printMaze(maze) # View Back Tracks

    return False


printMaze(MAZE)
solveMaze(MAZE)
printMaze(MAZE)



