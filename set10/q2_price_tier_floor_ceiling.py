# Title: Price Tier Floor and Ceiling
# Difficulty: Easy
# Scenario: A shop's price list contains the available price tiers in increasing order (the same tier may be listed
# more than once). A customer states a budget q. The shop wants to quote the most expensive tier not above
# the budget (floor) and the cheapest tier not below the budget (ceiling), so that it can suggest the nearest
# options on either side.
# Problem statement: Given a non-decreasing array of n prices and a query value q, print two values
# separated by a space: the floor (largest price ≤ q) and the ceiling (smallest price ≥ q). If a value does not
# exist print the word None in its place. Use binary search.
# Input format:
# Line 1: integer n.
# Line 2: n integers in non-decreasing order.
# Line 3: integer q.
# Output format:
# Print 'floor ceiling' where each is an integer or None.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • -10^9 ≤ price, q ≤ 10^9
# Sample input:
# 6
# 10 20 30 40 50 60
# 35
# Sample output:
# 30 40

n = int(input())
arr = list(map(int, input().split()))
q = int(input())

# Find floor: last element <= q
left = 0
right = n - 1
floor_value = None

while left <= right:
    mid = (left + right) // 2

    if arr[mid] <= q:
        floor_value = arr[mid]
        left = mid + 1
    else:
        right = mid - 1

# Find ceiling: first element >= q
left = 0
right = n - 1
ceiling_value = None

while left <= right:
    mid = (left + right) // 2

    if arr[mid] >= q:
        ceiling_value = arr[mid]
        right = mid - 1
    else:
        left = mid + 1

print(floor_value, ceiling_value)