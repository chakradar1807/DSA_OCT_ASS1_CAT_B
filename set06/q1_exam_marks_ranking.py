# Title: Exam Marks Ranking by Counting
# Difficulty: Easy
# Scenario: A university publishes the marks of n students for an exam out of 100. Every mark is a whole
# number from 0 to 100, but n can be very large (tens of thousands). The registrar wants all marks listed in
# ascending order as quickly as possible.
# Problem statement: Sort the n marks in non-decreasing order using counting sort: count how many times
# each mark 0..100 occurs, then rebuild the list from the counts. Built-in sorting and Counter are not allowed.
# Input format:
# Line 1: integer n.
# Line 2: n space-separated integers, the marks.
# Output format:
# Print the sorted marks on one line separated by spaces.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 0 ≤ mark ≤ 100
# Sample input:
# 10
# 78 92 65 78 100 0 65 92 78 55
# Sample output:
# 0 55 65 65 78 78 78 92 92 100


n = int(input())
marks = list(map(int, input().split()))

count = [0] * 101

for mark in marks:
    count[mark] += 1

result = []

for mark in range(101):
    for j in range(count[mark]):
        result += [mark]

print(*result)