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

if redShirt == 0 or blueShirt == 0:
    N = 1

if redSocks == 0 or blueSocks == 0:
    M = 1

print(N, M)
