# Title: Fastest Deliveries Podium
# Difficulty: Easy
# Scenario: A courier company logs the delivery time in minutes of n completed orders. A weekly report needs
# only the k fastest deliveries, listed from fastest to slowest. Sorting the whole log would waste effort when k is
# small.
# Problem statement: Given n delivery times and an integer k, print the k smallest times in non-decreasing
# order (duplicates count separately). Use selection-sort rounds: stop after k rounds instead of sorting
# everything. Built-in sorting, min() and heaps are not allowed.
# Input format:
# Line 1: integers n and k.
# Line 2: n space-separated integers, the delivery times.
# Output format:
# Print k integers on one line separated by spaces, in non-decreasing order.
# Constraints:
# • 1 ≤ k ≤ n ≤ 3000
# • 1 ≤ time ≤ 10^4
# Sample input:
# 7 3
# 29 14 36 7 21 14 50
# Sample output:
# 7 14 14

n, k = map(int, input().strip().split())
times = list(map(int, input().strip().split()))

for i in range(k):
    smallest = i

    for j in range(i + 1, n):
        if times[j] < times[smallest]:
            smallest = j

    temp = times[i]
    times[i] = times[smallest]
    times[smallest] = temp

for i in range(k):
    if i > 0:
        print(" ", end="")
    print(times[i], end="")

print()