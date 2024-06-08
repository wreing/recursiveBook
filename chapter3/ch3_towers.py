import sys

TOTAL_DISKS = 10
#Populate Tower A

TOWERS = {'A' : list(reversed(range(1, TOTAL_DISKS+1))),
          'B' : [],
          'C' : []}

def printDisk(diskNum):
    #print a single disk of width diskNum
    emptySpace = ' ' * (TOTAL_DISKS - diskNum)
    if diskNum == 0:
        # just draw pole
        sys.stdout.write(emptySpace + '||' + emptySpace)
    else:
        diskSpace =  '@' * diskNum
        diskNumLabel = str(diskNum).rjust(2, '_')
        sys.stdout.write(emptySpace + diskSpace + diskNumLabel + diskSpace + emptySpace)

def printTowers():
    #print all three towers
    for level in range(TOTAL_DISKS, -1,-1):
        for tower in (TOWERS['A'], TOWERS['B'], TOWERS['C']):
            if level >= len(tower):
                printDisk(0)
            else:
                printDisk(tower[level])
        sys.stdout.write('\n')
    # print tower labels A, B, C
    emptySpace = ' ' * (TOTAL_DISKS)
    print('%s A%s%s B%s%s C\n' %(emptySpace, emptySpace, emptySpace, emptySpace, emptySpace))

def moveOneDisk(startTower, endTower):
    #move the top disk from the start tower to the end tower
    disk = TOWERS[startTower].pop()
    TOWERS[endTower].append(disk)

def solve(numberOfDisks, startTower, tempTower, endTower):
    if numberOfDisks == 1:
        #BASE CASE
        moveOneDisk(startTower, endTower)
        printTowers()
        return
    else:
        # RECURSIVE CASE
        solve(numberOfDisks -1, startTower, endTower, tempTower)
        moveOneDisk(startTower, endTower)
        printTowers()
        solve(numberOfDisks -1, tempTower, startTower, endTower)
        return


printTowers()
solve(TOTAL_DISKS, 'A', 'B', 'C')

#while True:
#    printTowers()
#    print('Enter letter of start tower and the end tower. (A, B, C) or Q to quit.')
#    move = input().upper()
#    if move == 'Q':
#        sys.exit()
#    elif move[0] in 'ABC' and move[1] in 'ABC' and move[0] != move[1]:
#        moveOneDisk(move[0], move[1])





