# Title: Library Catalogue Lookup
# Difficulty: Easy
# Scenario: A university library keeps the book IDs on one shelf-row in strictly increasing order. The librarian's
# terminal must tell a student at which shelf position (0-based) a given book ID sits, or that the book is not on
# this row. Because there are thousands of books and many lookups per minute, scanning the row one book at
# a time is too slow.
# Problem statement: Given a strictly increasing array of n book IDs and a query ID q, print the 0-based index
# of q in the array, or -1 if q does not occur. Use binary search with lo, hi and mid = lo + (hi − lo) // 2; do not
# use bisect or list.index.
# Input format:
# Line 1: integer n.
# Line 2: n strictly increasing integers.
# Line 3: integer q, the book ID to find.
# Output format:
# Print one integer: the index of q, or -1.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • -10^9 ≤ ID, q ≤ 10^9
# • IDs are distinct and sorted in increasing order
# Sample input:
# 9
# 102 118 130 145 160 177 190 204 230
# 177
# Sample output:
# 5

n = int(input())
arr = list(map(int, input().split()))
q = int(input())

low = 0
high = n - 1
answer = -1

while low <= high:
    mid = low + (high - low) // 2

    if arr[mid] == q:
        answer = mid
        break

    elif arr[mid] < q:
        low = mid + 1

    else:
        high = mid - 1

print(answer)