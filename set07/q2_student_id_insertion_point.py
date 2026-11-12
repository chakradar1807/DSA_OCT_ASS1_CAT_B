# Title: Student ID Insertion Point
# Difficulty: Easy
# Scenario: A registrar keeps a sorted list of already-issued student IDs. When a new student arrives, the
# system must tell the clerk the position at which the new ID should be inserted to keep the list sorted. If the ID
# has already been issued, the system reports the position of that existing ID instead.
# Problem statement: Given a strictly increasing array of n IDs and a target t, print the index of t if it is
# present; otherwise print the index where t would have to be inserted to keep the array sorted (the number of
# elements smaller than t). Use binary search; do not use bisect.
# Input format:
# Line 1: integer n.
# Line 2: n strictly increasing integers.
# Line 3: integer t.
# Output format:
# Print one integer between 0 and n inclusive.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • -10^9 ≤ ID, t ≤ 10^9
# • IDs are distinct and sorted
# Sample input:
# 6
# 10 20 30 45 60 80
# 50
# Sample output:
# 4

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

low = 0
high = n

while low < high:
    mid = low + (high - low) // 2

    if arr[mid] < target:
        low = mid + 1
    else:
        high = mid

print(low)