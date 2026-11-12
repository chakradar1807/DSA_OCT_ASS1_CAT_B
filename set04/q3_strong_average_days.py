# Title: Strong Average Days
# Difficulty: Easy
# Scenario: A school records the number of students present each day for n days. A 'strong period' is any k
# consecutive days whose average attendance is at least T. The principal wants to know how many strong
# periods (windows) exist.
# Problem statement: Given n daily attendance counts, an integer k and a threshold T, print the number of
# windows of exactly k consecutive days whose average is at least T. To avoid fractions, a window qualifies
# when its sum is at least k·T. Overlapping windows are all counted.
# Input format:
# Line 1: integers n, k and T.
# Line 2: n space-separated integers, the daily counts.
# Output format:
# Print one integer: the number of qualifying windows.
# Constraints:
# • 1 ≤ k ≤ n ≤ 10^5
# • 0 ≤ count ≤ 10^4
# • 1 ≤ T ≤ 10^4
# Sample input:
# 8 3 4
# 2 2 2 2 5 5 5 8
# Sample output:
# 3

n, k, T = map(int, input().strip().split())
attendance = list(map(int, input().strip().split()))

current = 0

for i in range(k):
    current += attendance[i]

count = 0
required = k * T

if current >= required:
    count += 1

for i in range(k, n):
    current = current + attendance[i] - attendance[i - k]

    if current >= required:
        count += 1

print(count)
