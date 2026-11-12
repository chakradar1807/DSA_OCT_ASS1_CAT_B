# Title: Booking Overlap Consolidation
# Difficulty: Medium
# Scenario: A conference-room system receives n booking requests, each a closed time interval [start, end] in
# whole minutes, in arbitrary order. Overlapping bookings (and bookings that share an endpoint) are to be
# consolidated into single blocks so that facilities staff can see the busy periods of the room.
# Problem statement: Merge all intervals that overlap or touch (two closed intervals merge when they share
# at least one point, e.g. [1,4] and [4,5] merge into [1,5], whereas [1,4] and [5,6] do not). Print the resulting
# disjoint intervals in increasing order of start, one interval per line as 'start end'. Use your own sort; built-in sort
# functions are not allowed.
# Input format:
# Line 1: integer n.
# Next n lines: two integers start and end (start ≤ end).
# Output format:
# Print one merged interval per line as 'start end', ordered by start.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 0 ≤ start ≤ end ≤ 10^9
# Sample input:
# 6
# 8 10
# 1 3
# 2 6
# 15 18
# 17 20
# 6 7
# Sample output:
# 1 7
# 8 10
# 15 20

n = int(input())

intervals = [None] * n

for i in range(n):
    intervals[i] = tuple(map(int, input().split()))

source = intervals[:]
destination = [None] * n

# Sort intervals by start, then end
width = 1

while width < n:
    start = 0

    while start < n:
        mid = start + width
        end = start + 2 * width

        if mid > n:
            mid = n
        if end > n:
            end = n

        i = start
        j = mid
        k = start

        while i < mid and j < end:
            if source[i] <= source[j]:
                destination[k] = source[i]
                i += 1
            else:
                destination[k] = source[j]
                j += 1
            k += 1

        while i < mid:
            destination[k] = source[i]
            i += 1
            k += 1

        while j < end:
            destination[k] = source[j]
            j += 1
            k += 1

        start += 2 * width

    source, destination = destination, source
    width *= 2

# Merge overlapping intervals
result = [None] * n
count = 0

current_start = source[0][0]
current_end = source[0][1]

for i in range(1, n):
    start = source[i][0]
    end = source[i][1]

    if start <= current_end:
        if end > current_end:
            current_end = end
    else:
        result[count] = (current_start, current_end)
        count += 1

        current_start = start
        current_end = end

result[count] = (current_start, current_end)
count += 1

for i in range(count):
    print(result[i][0], result[i][1])