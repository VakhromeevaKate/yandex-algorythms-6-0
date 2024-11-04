import sys
import math

line1 = sys.stdin.readline().split(' ')
line2 = sys.stdin.readline().split(' ')

n = int(line1[0])
num = int(line1[1])
arr = []

for i in range(0, len(line2)):
    if (i < n):
        arr.append(int(line2[i]))

def count_hally_value_variants(arr, num):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] == num:
            count += 1
        else:
            sum = arr[i]
            for R in range(i + 1, len(arr)):
                sum += arr[R]
                if sum == num:
                    count += 1
                elif sum > num:
                    break
    return count

print(count_hally_value_variants(arr, num))
