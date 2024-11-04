import sys
import math

lines = []

for line in sys.stdin:
    if len(lines) < 4:
        lines.append(int(line))
    else:
        break

redShirt = lines[0]
blueShirt = lines[1]
redSocks = lines[2]
blueSocks = lines[3]

findColor = 'red'

minBlue = min(blueShirt, blueSocks)
minRed = min(redShirt, redSocks)
minShirt = min(blueShirt, redShirt)
minSocks = min(redSocks, blueSocks)
maxShirt = max(blueShirt, redShirt)
maxSocks = max(redSocks, blueSocks)

N = minShirt + 1
M = minSocks + 1

if minShirt != 0 and minSocks != 0:

    if redShirt + redSocks > blueShirt + blueSocks:
        N = blueShirt + 1
        M = 1 if blueShirt + 1 > maxShirt else minSocks + 1
    elif blueShirt + blueSocks > redShirt + redSocks:
        N = redShirt + 1
        M = 1 if redShirt + 1 > maxShirt else minShirt + 1
    elif redShirt + redSocks >= N + M:
            N = redShirt + 1
            M = redSocks + 1
    elif blueShirt + blueSocks >= N + M:
            N = blueShirt + 1
            M = blueSocks + 1
    else:
        if redShirt + redSocks >= blueShirt + blueSocks:
            N = maxShirt + 1
            M = 1
        else:
            N = 1
            M = maxSocks + 1

if redShirt == 0:
    N = 1
    M = redSocks + 1

if blueShirt == 0:
    N = 1
    M = blueSocks + 1

if redSocks == 0 and redShirt == 0:
    N = 1
    M = 1

if blueSocks == 0 and blueShirt == 0:
    N = 1
    M = 1

print(N, M)
