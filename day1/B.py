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

maxShirts = max(redShirt, blueShirt)
maxSocks = max(redSocks, blueSocks)

minShirts = min(redShirt, blueShirt)
minSocks = min(redSocks, blueSocks)

N = 1
M = 1

N1 = minShirts + 1
M1 = minSocks + 1

if minShirts == 0 and minSocks != 0:
    N = 1
    M = maxSocks + 1

elif minShirts != 0 and minSocks == 0:
    N = maxShirts + 1
    M = 1

elif minShirts == 0 and minSocks == 0:
    N = 1
    M = 1

if minShirts != 0 and minSocks != 0:

    if maxShirts >= maxSocks:
        N = minShirts + 1
        M = 1

    elif maxSocks > maxShirts:
        N = maxShirts + 1
        M = 1

    if N + M > N1 + M1:
        N = N1
        M = M1

print(N, M)
