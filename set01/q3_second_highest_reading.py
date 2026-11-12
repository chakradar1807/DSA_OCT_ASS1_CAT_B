# Title: Second Highest Sensor Reading
# Difficulty: Easy
# Scenario: A weather station records n temperature readings in one day. The station manager wants the
# second-highest distinct reading, to compare against the day's peak and judge how sharp the peak was.

# Problem statement: Given n integer readings (possibly negative and possibly repeated), print the second-
# largest distinct value. Distinct means equal values count once: for the readings 9 9 5 the second-largest

# distinct value is 5. If fewer than two distinct values exist, print the word None.
# Input format:
# Line 1: integer n.
# Line 2: n space-separated integers, the readings.
# Output format:
# Print one integer: the second-largest distinct reading, or the word None if it does not exist.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • -10^9 ≤ reading ≤ 10^9
# • Do not use built-in max, min, sum or sorting.
# Sample input:
# 9
# 31 28 35 35 29 -4 35 28 30
# Sample output:
# 31

n = int(input().strip())
readings = list(map(int, input().split()))

largest = None
second_largest = None

for value in readings:
    if largest is None or value > largest:
        if largest != value:
            second_largest = largest
            largest = value

    elif value != largest:
        if second_largest is None or value > second_largest:
            second_largest = value

if second_largest is None:
    print("None")
else:
    print(second_largest)