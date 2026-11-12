# Title: Repeated Login Alert
# Difficulty: Easy
# Scenario: A bank's login-monitoring system receives a stream of user IDs, one per login event. If the same
# user ID logs in twice within k events of each other (positions differing by at most k), the system raises a
# suspicious-activity alert.
# Problem statement: Given the n user IDs in event order and the integer k, print YES if there exist two
# different positions i < j with the same ID and j − i ≤ k; otherwise print NO.
# Input format:
# Line 1: integers n and k.
# Line 2: n space-separated integers, the user IDs.
# Output format:
# Print YES or NO.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 1 ≤ k ≤ 10^5
# • 1 ≤ ID ≤ 10^9
# Sample input:
# 8 2
# 7 12 5 7 12 9 12 4
# Sample output:
# YES

n, k = map(int, input().strip().split())
users = list(map(int, input().strip().split()))

last_position = {}
answer = "NO"

for i in range(n):
    user = users[i]

    if user in last_position:
        if i - last_position[user] <= k:
            answer = "YES"
            break

    last_position[user] = i

print(answer)