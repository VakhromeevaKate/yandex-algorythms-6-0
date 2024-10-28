import sys
import math

lines = []

for line in sys.stdin:
    if len(lines) < 6:
        lines.append(int(line))
    else:
        break

x1 = lines[0]
y1 = lines[1]
x2 = lines[2]
y2 = lines[3]
x = lines[4]
y = lines[5]

epsilon = 0.01

def x_dist():
    return 0 if x > x1 and x <x2 else min(abs(x - x1), abs(x - x2))

def y_dist():
    return 0 if y > y1 and y < y2 else min(abs(y - y1), abs(y - y2))

resDict = {
    'S': math.sqrt((y - y1)**2 + (x_dist() + epsilon)**2),
    'N': math.sqrt((y - y2)**2 + (x_dist() + epsilon)**2),
    'E': math.sqrt((x - x2)**2 + (y_dist() + epsilon)**2),
    'W': math.sqrt((x - x1)**2 + (y_dist() + epsilon)**2),

    'NW': math.sqrt((x - x1)**2 + (y - y2)**2),
    'NE': math.sqrt((x - x2)**2 + (y - y2)**2),
    'SW': math.sqrt((x - x1)**2 + (y - y1)**2),
    'SE': math.sqrt((x - x2)**2 + (y - y1)**2)
}

minVal = sys.float_info.max
minKey = ''

for key, value in resDict.items():
    if value < minVal:
        minVal = value
        minKey = key

print(minKey)
print(resDict)
