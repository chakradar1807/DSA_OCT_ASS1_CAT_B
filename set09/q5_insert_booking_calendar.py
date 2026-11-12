# Title: Insert a Booking into the Calendar
# Difficulty: Medium
# Scenario: A clinic's calendar for one doctor is a list of already consolidated bookings: closed intervals [start,
# end], sorted by start and pairwise disjoint (each start is strictly larger than the previous end). A new booking
# arrives and must be inserted; if it overlaps or touches existing bookings they must be merged into one block.
# Problem statement: Given n sorted, pairwise disjoint intervals and one new interval, print the updated
# calendar: all intervals still sorted and disjoint, with the new interval merged into any intervals that share at
# least one point with it. Print one interval per line as 'start end'. The existing list is already sorted, so no sorting
# is needed.
# Input format:
# Line 1: integer n.
# Next n lines: 'start end' for each existing interval.
# Last line: 'start end' of the new interval.
# Output format:
# Print the resulting intervals, one per line as 'start end', in increasing order.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 0 ≤ start ≤ end ≤ 10^9
# • Existing intervals are sorted by start and pairwise disjoint (non-touching)
# Sample input:
# 5
# 1 3
# 6 9
# 12 15
# 18 20
# 22 25
# 8 13
# Sample output:
# 1 3
# 6 15
# 18 20
# 22 25


n = int(input())

intervals = [None] * n

for i in range(n):
    intervals[i] = tuple(map(int, input().split()))

new_start, new_end = map(int, input().split())

result = [None] * (n + 1)
k = 0
i = 0

# Step 1: Copy intervals before the new interval
while i < n and intervals[i][1] < new_start:
    result[k] = intervals[i]
    k += 1
    i += 1

# Step 2: Merge overlapping or touching intervals
while i < n and intervals[i][0] <= new_end:

    if intervals[i][0] < new_start:
        new_start = intervals[i][0]

    if intervals[i][1] > new_end:
        new_end = intervals[i][1]

    i += 1

result[k] = (new_start, new_end)
k += 1

# Step 3: Copy remaining intervals
while i < n:
    result[k] = intervals[i]
    k += 1
    i += 1

for i in range(k):
    print(result[i][0], result[i][1])