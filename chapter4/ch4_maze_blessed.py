# std imports
from math import floor

# local
from blessed import Terminal
from time import sleep 

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

term = Terminal()


def printMaze(maze):
    # Draw the maze 2 characters in from the edge
    x_offset = 2 
    y_offset = 2
    sleep(.2)
    
    with term.cbreak(), term.hidden_cursor():
        # clear the screen
        print(term.home + term.black_on_plum + term.clear)
    
    
        # draw !
        for y in range(HEIGHT):
            txt_erase = term.move_xy(x_offset, y+y_offset) + ' '
            txt_line = term.move_xy(x_offset, y+y_offset) + ''.join(maze[y])
            print(txt_erase + txt_line, end='', flush=True)



        
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


with term.cbreak(), term.hidden_cursor():
    # I'd like to add a keyboard interupt to allow [q] to quit even if the maze isn't
    # solved but with the recuresive calls to print I'm not sure how to enable that
    x = solveMaze(MAZE)

