# Title: Budget Pairing in a Sorted Price List
# Difficulty: Easy
# Scenario: An online shop lists its products in non-decreasing order of price. A customer with a voucher of
# exact value T wants a two-item bundle whose prices add up to T exactly. The shop's server must answer
# instantly, even for catalogues with 10^5 items.
# Problem statement: Given n prices in non-decreasing order and the target T, find the two different positions
# (1-based, i < j) whose prices sum to T and print them separated by a space. The input guarantees exactly
# one such pair of positions. The same position cannot be used twice.
# Input format:
# Line 1: integer n.
# Line 2: n integers in non-decreasing order.
# Line 3: integer T.
# Output format:
# Print two integers i and j (1-based, i < j).
# Constraints:
# • 2 ≤ n ≤ 10^5
# • -10^9 ≤ price ≤ 10^9 (negative values represent refunds)
# • -2×10^9 ≤ T ≤ 2×10^9
# • Exactly one valid pair of positions exists
# • Do not use extra memory proportional to n
# Sample input:
# 7
# 3 8 12 19 25 31 40
# 44
# Sample output:
# 4 5


n = int(input())
arr = list(map(int, input().split()))
target = int(input())

left = 0
right = n - 1

while left < right:
    total = arr[left] + arr[right]

    if total == target:
        print(left + 1, right + 1)
        break

    elif total < target:
        left += 1

    else:
        right -= 1