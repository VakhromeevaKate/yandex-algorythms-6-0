import sys
import math
import math

n = int(sys.stdin.readline())
line = sys.stdin.readline().split(' ')

arr = []

for i in range(0, len(line)):
    if (i < n):
        arr.append(int(line[i]))

def count_min_moves(arr):
    mincount = math.inf
    for i in range(len(arr)):
        count = 0
        for p in range(len(arr)):
            if p != i:
                count += arr[p] * abs(p - i)
        if mincount > count:
            mincount = count
    return mincount

print(count_min_moves(arr))

