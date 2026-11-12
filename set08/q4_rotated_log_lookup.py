# Title: Rotated Log Lookup
# Difficulty: Medium
# Scenario: A logging service stores sequence numbers in a circular buffer. Logically the numbers are sorted,
# but the buffer's start pointer has moved, so physically the array is a sorted array rotated by an unknown
# offset. Support engineers need to find the physical position of a given sequence number quickly.
# Problem statement: Given a rotated sorted array of n distinct integers and a target t, print the index of t, or -
# 1 if t is absent, in O(log n) time. Do not first locate the rotation point with a linear scan and do not use built-in
# search methods.
# Input format:
# Line 1: integer n.
# Line 2: n distinct integers forming a rotated sorted array.
# Line 3: integer t.
# Output format:
# Print one integer: the index of t, or -1.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • -10^9 ≤ value, t ≤ 10^9
# • All values are distinct
# Sample input:
# 8
# 15 18 22 31 3 6 9 12
# 9
# Sample output:
# 6

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

low = 0
high = n - 1
answer = -1

while low <= high:
    mid = low + (high - low) // 2

    if arr[mid] == target:
        answer = mid
        break

    # Left half is sorted
    elif arr[low] <= arr[mid]:

        if arr[low] <= target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    # Right half is sorted
    else:

        if arr[mid] < target <= arr[high]:
            low = mid + 1
        else:
            high = mid - 1

print(answer)