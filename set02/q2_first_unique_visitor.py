# Title: First Unique Visitor
# Difficulty: Easy
# Scenario: A website logs visitor IDs in the order they open the landing page. The marketing team wants to
# follow up with the earliest visitor who visited exactly once in the whole log (a one-time visitor).
# Problem statement: Given the log of n visitor IDs, print the ID of the first visitor (by position in the log)
# whose ID occurs exactly once in the entire log. If every ID occurs at least twice, print -1.
# Input format:
# Line 1: integer n.
# Line 2: n space-separated positive integers, the visitor IDs in log order.
# Output format:
# Print one integer: the first non-repeating ID, or -1.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 1 ≤ ID ≤ 10^9
# Sample input:
# 10
# 17 23 17 8 23 42 8 5 42 17
# Sample output:
# 5


n = int(input())
visitors = list(map(int, input().split()))

frequency = {}

for visitor in visitors:
    if visitor in frequency:
        frequency[visitor] += 1
    else:
        frequency[visitor] = 1

answer = -1

for visitor in visitors:
    if frequency[visitor] == 1:
        answer = visitor
        break

print(answer)