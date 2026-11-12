# Title: Judges' Trimmed Mean
# Difficulty: Easy
# Scenario: In a talent contest n judges give integer scores. To reduce bias, the organisers discard the t
# lowest and the t highest scores and report the average of the remaining n − 2t scores, rounded to two
# decimals.
# Problem statement: Given the n scores and an integer t with n − 2t ≥ 1, discard the t smallest and the t
# largest scores (equal scores are interchangeable) and print the arithmetic mean of the remaining scores
# formatted with exactly two digits after the decimal point. Implement your own sorting routine; built-in sort
# functions are not allowed.
# Input format:
# Line 1: integers n and t.
# Line 2: n integers, the scores.
# Output format:
# Print the trimmed mean with exactly two decimals (use the format '%.2f').
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 0 ≤ t and n − 2t ≥ 1
# • 0 ≤ score ≤ 100
# Sample input:
# 10 1
# 8 9 7 10 6 9 5 8 9 10
# Sample output:
# 8.25


n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Bubble Sort
for i in range(n - 1):
    swapped = False

    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    if not swapped:
        break

total = 0

for i in range(t, n - t):
    total += arr[i]

count = n - 2 * t
average = total / count

print("%.2f" % average)