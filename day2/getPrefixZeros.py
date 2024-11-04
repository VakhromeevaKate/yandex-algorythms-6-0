import sys
import math

n = int(sys.stdin.readline())
line = sys.stdin.readline().split(' ')

arr = []

for i in range(0, len(line)):
    if (i < n):
        arr.append(int(line[i]))

def getprefixzeros(nums):
    prefixes = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        if nums[i - 1] == 0:
            prefixes[i] =  prefixes[i - 1] + 1
        else:
            prefixes[i] =  prefixes[i - 1]
    return prefixes[1:]

prefixzeros = getprefixzeros(arr)
print(prefixzeros)

def countzeros(prefixzeros, l, r):
    if (r > l):
        return prefixzeros[r] - prefixzeros[l]
    else:
        return 0


result = countzeros(prefixzeros, 0, 4)
print(result)

#print(' '.join(str(el) for el in result))