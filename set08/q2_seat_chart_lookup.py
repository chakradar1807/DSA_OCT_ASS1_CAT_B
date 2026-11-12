# Title: Seat Chart Lookup
# Difficulty: Easy
# Scenario: A cinema stores ticket numbers in an R × C seating chart. Each row is sorted from left to right,
# and the first ticket number of each row is larger than the last ticket number of the previous row. A usher
# scans a ticket and needs the seat (row and column) quickly.
# Problem statement: Given the R × C matrix with the properties above and a ticket number t, print the 0-
# based row and column of t, separated by a space, or -1 -1 if t is not in the chart. Treat the matrix as a sorted
# 1-D array of R·C elements and binary search it using index arithmetic (row = idx // C, col = idx % C); do not
# flatten into a new list.
# Input format:
# Line 1: integers R and C.
# Next R lines: C integers each (one row).
# Last line: integer t.
# Output format:
# Print 'row col' or '-1 -1'.
# Constraints:
# • 1 ≤ R, C ≤ 300
# • -10^9 ≤ value, t ≤ 10^9
# • All values are distinct; each row is increasing and the first value of each row exceeds the last value of
# the previous row
# Sample input:
# 3 4
# 1 3 5 7
# 10 11 16 20
# 23 30 34 60
# 16
# Sample output:
# 1 2


R, C = map(int, input().split())

matrix = []

for i in range(R):
    row = list(map(int, input().split()))
    matrix += [row]

target = int(input())

low = 0
high = R * C - 1
answer_row = -1
answer_col = -1

while low <= high:
    mid = low + (high - low) // 2

    row = mid // C
    col = mid % C

    if matrix[row][col] == target:
        answer_row = row
        answer_col = col
        break

    elif matrix[row][col] < target:
        low = mid + 1

    else:
        high = mid - 1

print(answer_row, answer_col)