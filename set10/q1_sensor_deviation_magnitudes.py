# Title: Sensor Deviation Magnitudes
# Difficulty: Easy
# Scenario: A calibration sensor reports deviations from a reference value, stored in increasing order, so
# negative deviations come first. Quality engineers need the squared deviations in increasing order as well, to
# see the smallest error magnitudes first.
# Problem statement: Given a non-decreasing array of n integers (possibly negative), print the squares of its
# elements in non-decreasing order. Squaring and then calling a built-in sort is not allowed; exploit the fact that
# the input is already sorted.
# Input format:
# Line 1: integer n.
# Line 2: n integers in non-decreasing order.
# Output format:
# Print n integers: the squares in non-decreasing order, separated by spaces.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • -10^4 ≤ value ≤ 10^4
# Sample input:
# 7
# -9 -4 -2 0 3 5 8
# Sample output:
# 0 4 9 16 25 64 81

n = int(input())
arr = list(map(int, input().split()))

result = [0] * n

left = 0
right = n - 1
pos = n - 1

while left <= right:
    left_square = arr[left] * arr[left]
    right_square = arr[right] * arr[right]

    if left_square > right_square:
        result[pos] = left_square
        left += 1
    else:
        result[pos] = right_square
        right -= 1

    pos -= 1

print(*result)