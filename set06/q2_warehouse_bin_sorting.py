# Title: Warehouse Bin Sorting
# Difficulty: Easy
# Scenario: A conveyor delivers parcels tagged 0 (fragile), 1 (standard) or 2 (heavy). Before loading, the
# parcels must be arranged so that all fragile ones come first, then standard, then heavy. The loading arm can
# only swap two parcels at a time and has no room for a second copy of the belt.
# Problem statement: Given n tags, each 0, 1 or 2, rearrange them in place into non-decreasing order and
# print the result. Aim for a single left-to-right pass using three pointers, without a general-purpose sort.
# Input format:
# Line 1: integer n.
# Line 2: n space-separated tags, each 0, 1 or 2.
# Output format:
# Print the rearranged tags on one line separated by spaces.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • Each tag is 0, 1 or 2
# Sample input:
# 8
# 2 0 1 2 1 0 1 0
# Sample output:
# 0 0 0 1 1 1 2 2

n = int(input())
arr = list(map(int, input().split()))

low = 0
mid = 0
high = n - 1

while mid <= high:
    if arr[mid] == 0:
        arr[low], arr[mid] = arr[mid], arr[low]
        low += 1
        mid += 1

    elif arr[mid] == 1:
        mid += 1

    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1

print(*arr)