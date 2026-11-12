# Title: Earliest Slot After Shift Change
# Difficulty: Easy
# Scenario: A hospital stores the start times (in minutes from midnight, all different) of appointment slots in
# increasing order, but after a shift change the rota was rotated: the list now starts in the middle of the original
# order and wraps around. The scheduler needs the earliest slot time, which is the minimum of the list.
# Problem statement: The array is a sorted array of distinct integers that has been rotated by some unknown
# amount (possibly zero). Print the minimum element in O(log n) time using binary search; do not use min() or
# a full scan.
# Input format:
# Line 1: integer n.
# Line 2: n distinct integers forming a rotated sorted array.
# Output format:
# Print one integer: the minimum value.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • -10^9 ≤ value ≤ 10^9
# • All values are distinct
# Sample input:
# 7
# 40 50 60 70 10 20 30
# Sample output:
# 10


n = int(input())
arr = list(map(int, input().split()))

low = 0
high = n - 1

while low < high:
    mid = low + (high - low) // 2

    if arr[mid] > arr[high]:
        low = mid + 1
    else:
        high = mid

print(arr[low])