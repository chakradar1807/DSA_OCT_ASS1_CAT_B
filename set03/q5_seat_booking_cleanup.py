# Title: Seat Booking Cleanup
# Difficulty: Medium
# Scenario: A theatre's booking table lists seat IDs in sorted order, one entry per booking. A seat may legally
# be booked at most twice (for the matinee and the evening show), but a software bug created extra duplicate
# entries. The cleanup tool must keep at most two entries per seat, preserve the order, and compact the table
# in place.
# Problem statement: Given a sorted (non-decreasing) array of n seat IDs, remove extra duplicates in place
# so that every distinct value appears at most twice, keeping the first two occurrences. Print k, the length of the
# cleaned list, and then the first k values of the modified array.
# Input format:
# Line 1: integer n.
# Line 2: n space-separated integers in non-decreasing order.
# Output format:
# Line 1: the integer k.
# Line 2: the k remaining values separated by spaces.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 1 ≤ seat ID ≤ 10^9
# • The array is sorted; no extra array may be created for the final answer
# Sample input:
# 10
# 1 1 1 2 2 3 3 3 3 4
# Sample output:
# 7
# 1 1 2 2 3 3 4

n = int(input())
seats = list(map(int, input().split()))

if n <= 2:
    k = n

else:
    k = 2

    for i in range(2, n):

        if seats[i] != seats[k - 2]:
            seats[k] = seats[i]
            k += 1

print(k)

for i in range(k):
    if i > 0:
        print(" ", end="")
    print(seats[i], end="")

print()