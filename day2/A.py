import sys
import math

n = int(sys.stdin.readline())
line = sys.stdin.readline().split(' ')

arr = []

for i in range(0, len(line)):
    if (i < n):
        arr.append(int(line[i]))

def prefixsum(nums):
    prefixes = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefixes[i] = prefixes[i - 1] + nums[i - 1]
    return prefixes[1:]

prefsum = prefixsum(arr)

print(' '.join(str(el) for el in prefsum))
