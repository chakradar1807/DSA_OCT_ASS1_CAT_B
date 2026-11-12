# Title: Campus Election Winner
# Difficulty: Easy
# Scenario: In a student-council election, every ballot carries a single candidate ID. The election rules say a
# candidate wins outright only by receiving strictly more than half of all ballots, and the returning officer has
# already verified that such a candidate exists in this round.
# Problem statement: Given the n candidate IDs written on the ballots, find and print the ID that appears
# strictly more than n/2 times. The input guarantees such an ID exists and is unique. ⌊ ⌋
# Input format:
# Line 1: integer n, the number of ballots.
# Line 2: n space-separated integers, the candidate IDs.
# Output format:
# Print one integer: the winning candidate ID.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 1 ≤ ID ≤ 10^9
# • A candidate with more than n/2 ballots always exists ⌊ ⌋
# Sample input:
# 9
# 3 2 3 3 1 3 2 3 3
# Sample output:
# 3

n = int(input())
votes = list(map(int, input().split()))

candidate = 0
count = 0

for vote in votes:
    if count == 0:
        candidate = vote
        count = 1
    elif vote == candidate:
        count += 1
    else:
        count -= 1

print(candidate)