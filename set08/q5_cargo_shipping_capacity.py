# Title: Cargo Shipping Capacity
# Difficulty: Medium
# Scenario: A freight company must ship n packages waiting in a fixed order at a depot. Each day the ship
# loads packages in that order (no reordering), up to its weight capacity, and sails. All packages must be
# delivered within D days. The company wants to charter the smallest possible ship capacity that makes this
# feasible.
# Problem statement: Given the package weights in shipping order and D, print the minimum ship capacity C
# such that the packages can be shipped in order, each day carrying a consecutive group of packages whose
# total weight does not exceed C, using at most D days. The capacity must be at least the weight of the
# heaviest package.
# Input format:
# Line 1: integers n and D.
# Line 2: n integers, the weights in shipping order.
# Output format:
# Print one integer: the minimum capacity.
# Constraints:
# • 1 ≤ D ≤ n ≤ 5 × 10^4
# • 1 ≤ weight ≤ 500
# • Do not use built-in max() or sum()
# Sample input:
# 7 3
# 4 2 7 1 8 3 5
# Sample output:
# 13

n, D = map(int, input().split())
weights = list(map(int, input().split()))

low = weights[0]
high = 0

for weight in weights:
    if weight > low:
        low = weight

    high += weight

answer = high

while low <= high:
    capacity = low + (high - low) // 2

    days = 1
    current_weight = 0

    for weight in weights:
        if current_weight + weight <= capacity:
            current_weight += weight
        else:
            days += 1
            current_weight = weight

    if days <= D:
        answer = capacity
        high = capacity - 1
    else:
        low = capacity + 1

print(answer)