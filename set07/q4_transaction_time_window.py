# Title: Transaction Time Window
# Difficulty: Medium
# Scenario: A payment system stores transaction amounts of one merchant in sorted order (many
# transactions share the same amount, for example fixed-price tickets). An auditor wants to know where the
# block of transactions with a given amount starts and ends in the sorted list, to inspect that block.
# Problem statement: Given a non-decreasing array of n amounts and a target x, print the 0-based index of
# the first occurrence of x and the index of the last occurrence, separated by a space. If x does not occur, print
# -1 -1. Use two binary searches; do not scan linearly and do not use bisect.
# Input format:
# Line 1: integer n.
# Line 2: n integers in non-decreasing order.
# Line 3: integer x.
# Output format:
# Print two integers: first index and last index, or -1 -1.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • -10^9 ≤ amount, x ≤ 10^9
# • The array may contain duplicates
# Sample input:
# 10
# 5 7 7 8 8 8 8 10 12 12
# 8
# Sample output:
# 3 6

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

# Find first occurrence
low = 0
high = n - 1
first = -1

while low <= high:
    mid = low + (high - low) // 2

    if arr[mid] == target:
        first = mid
        high = mid - 1

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

# Find last occurrence
low = 0
high = n - 1
last = -1

while low <= high:
    mid = low + (high - low) // 2

    if arr[mid] == target:
        last = mid
        low = mid + 1

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

print(first, last)