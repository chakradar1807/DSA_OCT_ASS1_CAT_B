# Title: Square Tile Floor Planner
# Difficulty: Easy
# Scenario: A contractor has x identical square floor tiles and wants to lay them as one large square block of s
# × s tiles. She wants the largest whole-number side s such that s × s tiles are available. The number of tiles
# can be astronomically large for industrial floors, so trying every side length one by one is too slow.
# Problem statement: Given a non-negative integer x, print the largest integer s such that s × s ≤ x (the floor
# of the square root of x). Do not use the sqrt function, math.isqrt or the ** 0.5 trick; use binary search over the
# possible values of s.
# Input format:
# A single line containing the integer x.
# Output format:
# Print one integer s.
# Constraints:
# • 0 ≤ x ≤ 10^18
# Sample input:
# 99
# Sample output:
# 9

x = int(input())

low = 0
high = x
answer = 0

while low <= high:
    mid = low + (high - low) // 2

    if mid * mid <= x:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)