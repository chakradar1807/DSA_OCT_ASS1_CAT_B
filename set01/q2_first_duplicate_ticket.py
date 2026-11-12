# Title: First Duplicate Ticket Scan
# Difficulty: Easy
# Scenario: At the gate of a campus fest, a scanner records each ticket ID as people walk in. A ticket must
# only be used once. Security wants to know the ID of the first scan that turns out to be a repeat of an earlier
# scan, so they can stop that person.
# Problem statement: Given the sequence of n scanned ticket IDs in scan order, print the ID of the earliest
# scan whose value has already appeared at an earlier position. If no ID repeats, print -1. (Note: the answer is
# determined by the position of the second occurrence, not the first occurrence.)
# Input format:
# Line 1: integer n, the number of scans.
# Line 2: n space-separated integers, the ticket IDs in scan order.
# Output format:
# Print a single integer: the ticket ID of the first repeated scan, or -1.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 1 ≤ ID ≤ 10^9
# Sample input:
# 8
# 4021 3377 5120 3377 4021 9001 5120 7
# Sample output:
# 3377



n = int(input().strip())
ticket_ids = list(map(int, input().split()))

seen = set()
answer = -1

for ticket_id in ticket_ids:
    if ticket_id in seen:
        answer = ticket_id
        break

    seen.add(ticket_id)

print(answer)