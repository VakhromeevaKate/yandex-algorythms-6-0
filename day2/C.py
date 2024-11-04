import sys
import math
import math

line1 = sys.stdin.readline().split(' ')
line2 = sys.stdin.readline().split(' ')

arr = []
points_quantyty = int(line1[0])
min_distance = int(line1[1])
distances = []


for i in range(0, len(line2)):
    distances.append(int(line2[i]))

# def prefixsub(nums):
#     prefixes = [0] * (len(nums))
#     for i in range(1, len(nums)):
#         prefixes[i] = nums[i] - nums[i - 1]
#     return prefixes[1:]

def count_ways(pref_distances, min_dist):
    maxcount = 0

    for i in range(len(pref_distances) - 1):
        for j in range(i + 1, len(pref_distances)):
            if pref_distances[j] - pref_distances[i] > min_dist:
                maxcount += 1
    return maxcount

print(count_ways(distances, min_distance))

