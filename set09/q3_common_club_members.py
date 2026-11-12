# Title: Common Club Members
# Difficulty: Easy
# Scenario: Two campus clubs have separate sign-up sheets of student IDs, in no particular order, and some
# students signed up several times. The student-affairs office wants the list of students who appear on both
# sheets, with each student listed once, in increasing order of ID.
# Problem statement: Given arrays A (m IDs) and B (n IDs), print the distinct IDs that occur in both arrays, in
# increasing order separated by spaces. If there is no common ID print None. Use a hash set for the
# membership test and your own sorting routine for the output; do not use set operators (&, |, -), sorted() or
# list.sort().
# Input format:
# Line 1: integers m and n.
# Line 2: m integers (sheet A).
# Line 3: n integers (sheet B).
# Output format:
# Common distinct IDs in increasing order on one line, or None.
# Constraints:
# • 1 ≤ m, n ≤ 10^5
# • 1 ≤ ID ≤ 10^9
# Sample input:
# 6 6
# 9 4 9 5 12 4
# 12 9 9 8 4 12
# Sample output:
# 4 9 12


m, n = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

set_A = set(A)
seen = set()

result = [0] * min(m, n)
k = 0

for value in B:
    if value in set_A and value not in seen:
        result[k] = value
        k += 1
        seen.add(value)

if k == 0:
    print("None")

else:
    source = result[:k]
    destination = [0] * k

    width = 1

    while width < k:
        start = 0

        while start < k:
            mid = start + width
            end = start + 2 * width

            if mid > k:
                mid = k
            if end > k:
                end = k

            i = start
            j = mid
            p = start

            while i < mid and j < end:
                if source[i] <= source[j]:
                    destination[p] = source[i]
                    i += 1
                else:
                    destination[p] = source[j]
                    j += 1
                p += 1

            while i < mid:
                destination[p] = source[i]
                i += 1
                p += 1

            while j < end:
                destination[p] = source[j]
                j += 1
                p += 1

            start += 2 * width

        source, destination = destination, source
        width *= 2

    print(*source)