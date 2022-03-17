import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
sx=0
sy=0
ex = w-1
ey = h-1
##sx,ex,sy,ey
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if(bomb_dir=="U"):
        ey = y0 - 1
    elif(bomb_dir=="UR"):
        sx = x0 + 1
        ey = y0 - 1
    elif(bomb_dir=="R"):
        sx = x0 + 1
    elif(bomb_dir=="DR"):
        sx = x0 + 1
        sy = y0 + 1
    elif(bomb_dir=="D"):
        sy = y0 + 1
    elif(bomb_dir=="DL"):
        ex = x0 - 1
        sy = y0 + 1
    elif(bomb_dir=="L"):
        ex = x0 - 1
    elif(bomb_dir=="UL"):
        ex = x0 - 1
        ey = y0 - 1
    if(sx<=ex):
        x0 = sx + (ex - sx)//2
    if(sy<=ey):
        y0 = sy + (ey - sy)//2
    print(str(x0)+" "+str(y0))

    # the location of the next window Batman should jump to.
    
