# Title: Textbook Allocation for Reading Groups
# Difficulty: Medium
# Scenario: A library has n textbooks arranged on a shelf in a fixed order with known page counts. The
# professor splits the class into m reading groups. Each group is given a contiguous block of books from the
# shelf (no group is left without books, and no book is split). She wants the heaviest group workload, measured
# in total pages, to be as small as possible.
# Problem statement: Given the page counts of the n books in shelf order and the number of groups m,
# assign contiguous blocks of books to the m groups so that every group receives at least one book and every
# book is assigned. Print the minimum possible value of the largest total number of pages given to any group.
# If m > n it is impossible to give every group a book; print -1.
# Input format:
# Line 1: integers n and m.
# Line 2: n integers, the page counts in shelf order.
# Output format:
# Print one integer: the minimised maximum pages, or -1 if m > n.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 1 ≤ m ≤ 10^5
# • 1 ≤ pages ≤ 10^4
# • Do not use built-in max() or sum()
# Sample input:
# 6 3
# 25 46 28 49 24 20
# Sample output:
# 77


n, m = map(int, input().split())
pages = list(map(int, input().split()))

if m > n:
    print(-1)

else:
    low = pages[0]
    high = 0

    i = 0
    while i < n:
        if pages[i] > low:
            low = pages[i]

        high += pages[i]
        i += 1

    answer = high

    while low <= high:
        capacity = (low + high) // 2

        groups = 1
        current_pages = 0

        i = 0
        while i < n:
            if current_pages + pages[i] <= capacity:
                current_pages += pages[i]
            else:
                groups += 1
                current_pages = pages[i]

            i += 1

        if groups <= m:
            answer = capacity
            high = capacity - 1
        else:
            low = capacity + 1

    print(answer)