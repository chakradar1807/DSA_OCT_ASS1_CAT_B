# Title: Merge Two Warehouse Stock Lists
# Difficulty: Medium
# Scenario: Warehouse A holds its item codes in a sorted list that already has spare empty slots at the end
# (marked 0), exactly enough to hold all item codes from warehouse B, whose own list is also sorted. The
# system must merge B's codes into A's list so that A's list becomes one sorted list, without allocating a third
# list.

# Problem statement: You are given m, n, an array A of length m+n whose first m entries are sorted (non-
# decreasing) and whose last n entries are placeholder zeros, and a sorted array B of n entries. Merge B into

# A so that A holds all m+n values in non-decreasing order, and print A. The placeholders are not real data;
# they must not appear in the result unless a real value equals 0. Do not use built-in sorting.
# Input format:
# Line 1: integers m and n.
# Line 2: m+n integers (the first m are sorted real values, the last n are 0 placeholders).
# Line 3: n integers, the sorted array B (an empty line if n = 0).
# Output format:
# Print the m+n merged values on one line, separated by spaces.
# Constraints:
# • 0 ≤ m, n ≤ 10^5, m + n ≥ 1
# • -10^9 ≤ value ≤ 10^9
# • Both input lists are sorted in non-decreasing order
# Sample input:
# 4 3
# 1 4 7 10 0 0 0
# 2 5 8
# Sample output:
# 1 2 4 5 7 8 10

m, n = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

i = m - 1
j = n - 1
k = m + n - 1

while j >= 0:

    if i >= 0 and A[i] > B[j]:
        A[k] = A[i]
        i -= 1

    else:
        A[k] = B[j]
        j -= 1

    k -= 1

for i in range(m + n):
    if i > 0:
        print(" ", end="")
    print(A[i], end="")

print()