# Title: Peak Traffic Window
# Difficulty: Easy
# Scenario: A news website records the number of visitors for each of n consecutive hours. The operations
# team wants to schedule server upgrades away from the busiest period, defined as the k consecutive hours
# with the highest total visitors.
# Problem statement: Given the hourly visitor counts and the window length k, print the largest possible total
# visitors over any k consecutive hours. Do not use built-in sum(), max() or slicing inside the loop; maintain the
# window total incrementally.
# Input format:
# Line 1: integers n and k.
# Line 2: n space-separated integers, the hourly visitor counts.
# Output format:
# Print one integer: the maximum window total.
# Constraints:
# • 1 ≤ k ≤ n ≤ 10^5
# • -10^4 ≤ count ≤ 10^4 (negative values represent corrections)
# Sample input:
# 9 3
# 4 2 10 1 3 9 6 5 7
# Sample output:
# 20

n, k = map(int, input().strip().split())
visitors = list(map(int, input().strip().split()))

current = 0

for i in range(k):
    current += visitors[i]

largest = current

for i in range(k, n):
    current = current + visitors[i] - visitors[i - k]

    if current > largest:
        largest = current

print(largest)