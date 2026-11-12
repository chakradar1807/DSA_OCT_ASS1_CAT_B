# Title: Nearly Sorted Event Log
# Difficulty: Easy
# Scenario: A server writes event timestamps almost in order, but network delays make a few events arrive
# late. Before storing the log, the system repairs the order with insertion sort and records how much repair
# work (element shifts) was needed as a measure of the delay problem.
# Problem statement: Sort the n timestamps in non-decreasing order using insertion sort (take each element

# and move it left past every strictly greater element). Print the sorted list and the total number of single-
# position shifts performed, where moving one element one place to the right counts as one shift. Built-in

# sorting is not allowed.
# Input format:
# Line 1: integer n.
# Line 2: n space-separated integers, the timestamps.
# Output format:
# Line 1: the sorted timestamps.
# Line 2: the total number of shifts.
# Constraints:
# • 1 ≤ n ≤ 5000
# • 0 ≤ timestamp ≤ 10^6
# Sample input:
# 8
# 10 20 15 30 40 35 50 45
# Sample output:
# 10 15 20 30 35 40 45 50
# 3

n = int(input().strip())
timestamps = list(map(int, input().strip().split()))

shifts = 0

for i in range(1, n):
    current = timestamps[i]
    j = i - 1

    while j >= 0 and timestamps[j] > current:
        timestamps[j + 1] = timestamps[j]
        shifts += 1
        j -= 1

    timestamps[j + 1] = current

for i in range(n):
    if i > 0:
        print(" ", end="")
    print(timestamps[i], end="")

print()
print(shifts)