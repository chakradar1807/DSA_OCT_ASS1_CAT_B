# Title: Daily Sales Range Reports
# Difficulty: Medium
# Scenario: A shop keeps the sales total for each of n days. The owner repeatedly asks for the total sales
# between two days (inclusive), for example 'what did we sell from day 3 to day 17?'. The daily numbers never
# change, but many queries arrive, so each answer must be fast.
# Problem statement: Given the n daily sales and q queries, each query being two 0-based indices l and r (l ≤
# r), print the sum of sales[l..r] for every query, one answer per line, in query order.
# Input format:
# Line 1: integers n and q.
# Line 2: n space-separated integers, the daily sales.
# Next q lines: two integers l and r per line.
# Output format:
# Print q lines; line k holds the answer to the k-th query.
# Constraints:
# • 1 ≤ n, q ≤ 10^5
# • 0 ≤ sales[i] ≤ 10^4
# • 0 ≤ l ≤ r ≤ n − 1
# • Built-in sum() and itertools.accumulate are not allowed
# Sample input:
# 8 4
# 5 3 8 2 7 1 9 4
# 0 2
# 3 5
# 1 7
# 4 4
# Sample output:
# 16
# 10
# 34
# 7

n, q = map(int, input().split())
sales = list(map(int, input().split()))

prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] + sales[i]

for i in range(q):
    l, r = map(int, input().split())

    answer = prefix[r + 1] - prefix[l]

    print(answer)