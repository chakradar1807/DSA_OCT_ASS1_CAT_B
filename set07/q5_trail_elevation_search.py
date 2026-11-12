# Title: Trail Elevation Search
# Difficulty: Medium
# Scenario: A hiking app records the altitude (in metres) at consecutive checkpoints along a trail that climbs
# strictly to a single summit and then descends strictly. Hikers ask 'at which checkpoint do I first reach altitude
# h?'. Because a checkpoint is read from a slow sensor log, the app wants to examine as few checkpoints as
# possible.
# Problem statement: The array is a mountain: strictly increasing up to a unique peak, then strictly
# decreasing (n ≥ 3, the peak is neither the first nor the last element). Given a target h, print the smallest index

# whose value is h, or -1 if h does not occur. Do it in O(log n): find the peak by binary search, then binary-
# search the increasing part, and only if needed the decreasing part.

# Input format:
# Line 1: integer n.
# Line 2: n integers forming a mountain.
# Line 3: integer h.
# Output format:
# Print one integer: the smallest index with value h, or -1.
# Constraints:
# • 3 ≤ n ≤ 10^5
# • -10^9 ≤ altitude, h ≤ 10^9
# • Strictly increasing then strictly decreasing, with the peak strictly inside
# Sample input:
# 9
# 2 5 9 14 20 17 11 6 1
# 11
# Sample output:
# 6

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

# Step 1: Find peak
low = 0
high = n - 1

while low < high:
    mid = low + (high - low) // 2

    if arr[mid] < arr[mid + 1]:
        low = mid + 1
    else:
        high = mid

peak = low

# Step 2: Search increasing part
low = 0
high = peak
answer = -1

while low <= high:
    mid = low + (high - low) // 2

    if arr[mid] == target:
        answer = mid
        break

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

# Step 3: Search decreasing part if not found
if answer == -1:
    low = peak + 1
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            answer = mid
            break

        elif arr[mid] > target:
            low = mid + 1

        else:
            high = mid - 1

print(answer)