# Title: Sensor Readings with Heavy Duplicates
# Difficulty: Medium
# Scenario: A factory sensor reports a quantised reading (a small integer level) every second, so a day's data
# contains many repeated values and only a few distinct ones. Analysts want the readings sorted in ascending
# order. A sort that treats equal readings badly would waste time on the duplicates, so the team wants a
# quicksort that groups all readings equal to the pivot together in one step.
# Problem statement: Sort the n readings in non-decreasing order using quicksort with 3-way (Dutch-flag)
# partitioning: elements smaller than the pivot, equal to the pivot and larger than the pivot are separated, and
# only the smaller and larger parts are sorted further. Use an explicit stack of index ranges (no recursion) and
# choose the middle element of each range as pivot. Built-in sorting is not allowed.
# Input format:
# Line 1: integer n.
# Line 2: n space-separated integers, the readings.
# Output format:
# Print the sorted readings on one line separated by spaces.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 0 ≤ reading ≤ 10^9 (typically only a few distinct values)
# Sample input:
# 10
# 3 1 3 2 3 1 2 3 1 3
# Sample output:
# 1 1 1 2 2 3 3 3 3 3

n = int(input())
arr = list(map(int, input().split()))

stack = [(0, n - 1)]

while len(stack) > 0:
    low, high = stack.pop()

    if low >= high:
        continue

    pivot = arr[(low + high) // 2]

    less = low
    current = low
    greater = high

    while current <= greater:
        if arr[current] < pivot:
            arr[less], arr[current] = arr[current], arr[less]
            less += 1
            current += 1

        elif arr[current] > pivot:
            arr[current], arr[greater] = arr[greater], arr[current]
            greater -= 1

        else:
            current += 1

    if low < less - 1:
        stack += [(low, less - 1)]

    if greater + 1 < high:
        stack += [(greater + 1, high)]

print(*arr)