# Title: Longest Attendance Streak
# Difficulty: Easy
# Scenario: A college tracks daily attendance counts for a class over n days. A 'good day' is a day with at
# least T students present. The department rewards classes with long unbroken runs of good days.
# Problem statement: Given the n daily attendance counts and the threshold T, print the length of the longest
# run of consecutive days in which every day has attendance ≥ T. If there is no good day, print 0.
# Input format:
# Line 1: two integers n and T.
# Line 2: n space-separated integers, the daily attendance counts.
# Output format:
# Print one integer: the longest streak length.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 1 ≤ T ≤ 10^4
# • 0 ≤ attendance ≤ 10^4
# Sample input:
# 10 30
# 28 35 40 31 30 12 33 36 29 41
# Sample output:
# 4

n, T = map(int, input().split())
attendance = list(map(int, input().split()))

current = 0
longest = 0

for value in attendance:
    if value >= T:
        current += 1

        if current > longest:
            longest = current
    else:
        current = 0

print(longest)