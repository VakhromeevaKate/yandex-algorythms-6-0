import sys
import math

n = int(sys.stdin.readline())
line = sys.stdin.readline().split(' ')

arr = []

for i in range(0, len(line)):
    if (i < n):
        arr.append(int(line[i]))

sum = 0

for i in range(0, len(arr) - 2):
    for j in range(i + 1, len(arr) - 1):
        for k in range (j + 1, len(arr)):
            mult = arr[i] * arr[j] * arr[k]
            sum = sum + mult

print(sum % 1000000007)
