# Title: Combined Attendee List
# Difficulty: Easy
# Scenario: Two student clubs each keep a sorted list of the student IDs who registered for their own
# workshop (no ID repeated within one list). The organisers want one combined invitation list in ascending
# order where a student who registered in both clubs appears only once.
# Problem statement: Given two strictly increasing lists A (m IDs) and B (n IDs), print the union of the two lists
# in strictly increasing order, with each ID printed once. If both lists are empty, print an empty line (this does
# not occur in the tests). Built-in sorting is not allowed; exploit the fact that both inputs are already sorted.
# Input format:
# Line 1: integers m and n.
# Line 2: m space-separated integers (list A; empty line if m = 0).
# Line 3: n space-separated integers (list B; empty line if n = 0).
# Output format:
# Print the merged distinct IDs on one line separated by spaces.
# Constraints:
# • 0 ≤ m, n ≤ 10^5, m + n ≥ 1
# • 1 ≤ ID ≤ 10^9
# • Each input list is strictly increasing
# Sample input:
# 5 4
# 3 8 12 20 25
# 5 8 20 31
# Sample output:
# 3 5 8 12 20 25 31

m, n = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

i = 0
j = 0
result = []

while i < m and j < n:
    if A[i] < B[j]:
        result += [A[i]]
        i += 1

    elif A[i] > B[j]:
        result += [B[j]]
        j += 1

    else:
        result += [A[i]]
        i += 1
        j += 1

while i < m:
    result += [A[i]]
    i += 1

while j < n:
    result += [B[j]]
    j += 1

print(*result)