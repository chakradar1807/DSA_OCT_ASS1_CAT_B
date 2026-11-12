# Title: Warehouse Balance Point
# Difficulty: Medium
# Scenario: A warehouse has n shelves in one aisle. Each shelf records a net stock change for the day
# (positive for received goods, negative for returns and write-offs). The supervisor wants a 'balance shelf': a
# shelf where the total change on all shelves strictly to its left equals the total change on all shelves strictly to
# its right, so the aisle can be audited as two balanced halves.
# Problem statement: Given the n net stock changes, find the leftmost index p (0-based) such that the sum of
# the elements with index smaller than p equals the sum of the elements with index larger than p. An empty
# side has sum 0. Print p, or -1 if no such index exists. The element at p itself belongs to neither side.
# Input format:
# Line 1: integer n.
# Line 2: n space-separated integers, the net stock changes.
# Output format:
# Print one integer: the leftmost balance index, or -1.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • -1000 ≤ change ≤ 1000
# Sample input:
# 6
# 3 -2 5 4 1 5
# Sample output:
# 3

n = int(input().strip())
changes = list(map(int, input().split()))

total = 0

for value in changes:
    total += value

left_sum = 0
answer = -1

for i in range(n):
    right_sum = total - left_sum - changes[i]

    if left_sum == right_sum:
        answer = i
        break

    left_sum += changes[i]

print(answer)