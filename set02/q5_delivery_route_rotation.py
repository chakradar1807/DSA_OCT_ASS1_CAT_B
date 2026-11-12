# Title: Delivery Route Rotation
# Difficulty: Medium
# Scenario: A courier company schedules n delivery stops for a driver. To balance workload, each new day's
# route is the previous day's route rotated to the right by k stops: the last k stops move to the front, and all
# other stops shift right keeping their order. Memory on the driver's handheld device is tiny, so the rotation
# must be done inside the same array without allocating another full-size list.
# Problem statement: Given the route (stop IDs in order) and the integer k, print the route after rotating it to
# the right by k positions. The value k may be 0, equal to n or larger than n; rotating by n returns the original
# order. Slicing tricks such as a[k:] + a[:k] and list reversal helpers are not allowed; reverse with explicit loops
# and swaps.
# Input format:
# Line 1: two integers n and k.
# Line 2: n space-separated integers, the stop IDs.
# Output format:
# Print the rotated route as n space-separated integers on one line.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 0 ≤ k ≤ 10^9
# • 1 ≤ stop ID ≤ 10^9
# Sample input:
# 7 3
# 1 2 3 4 5 6 7
# Sample output:
# 5 6 7 1 2 3 4


n, k = map(int, input().split())
route = list(map(int, input().split()))

k = k % n

# Reverse the entire array
left = 0
right = n - 1

while left < right:
    temp = route[left]
    route[left] = route[right]
    route[right] = temp

    left += 1
    right -= 1

# Reverse the first k elements
left = 0
right = k - 1

while left < right:
    temp = route[left]
    route[left] = route[right]
    route[right] = temp

    left += 1
    right -= 1

# Reverse the remaining elements
left = k
right = n - 1

while left < right:
    temp = route[left]
    route[left] = route[right]
    route[right] = temp

    left += 1
    right -= 1

for i in range(n):
    if i > 0:
        print(" ", end="")
    print(route[i], end="")

print()