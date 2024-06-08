
import sys

# Create the image
im = [list('..#######################............'),
      list('..#.....................#............'),
      list('..#.....................#...#####....'),
      list('..#..........######.....#####...#....'),
      list('..#..........#....#.............#....'),
      list('..#..........######....0.....####....'),
      list('..#######....................#.......'),
      list('........#..#####........######.......'),
      list('........####...##########............'),
      list('.....................................')]

# Create the image
im = [list('..#######################............'),
      list('..#........#............#............'),
      list('..#........#......####..#...#####....'),
      list('..#........#.######..#..#####...#....'),
      list('..#......###.#....####..........#....'),
      list('..#......#...######.........####.....'),
      list('..########...................#.......'),
      list('........#..#####........######.......'),
      list('........####...##########............'),
      list('.....................................')]

HEIGHT = len(im)
WIDTH = len(im[0])

def printImage(image):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            sys.stdout.write(image[y][x])
        sys.stdout.write('\n')
    sys.stdout.write('\n')


def floodFill(image, x, y, newChar, oldChar=None):
    if oldChar == None:
        oldChar = im[y][x]
    #BASE CASE
    # Change x,y to newChar
    if im[y][x] != oldChar:
        return

    # RECURSIVE CASE
    # change x, y to newChar
    im[y][x] = newChar 

    # Call FloodFill on each adjacent cordinate
    if y-1>=0 :
        floodFill(im, x, y-1, newChar, oldChar)
    if y+1<HEIGHT :
        floodFill(im, x, y+1, newChar, oldChar)
    if x-1>=0 :
        floodFill(im, x-1, y, newChar, oldChar)
    if x+1<WIDTH :
        floodFill(im, x+1, y, newChar, oldChar)
    return

def countRooms(image):
    countOfRooms = 0
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if image[y][x] == '.':
                floodFill(image, x, y, '#')
                countOfRooms = countOfRooms + 1
                print(countOfRooms)
                printImage(image)
    return countOfRooms
                

printImage(im)
countRooms(im)

