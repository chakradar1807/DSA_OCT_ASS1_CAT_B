# Title: Mock Test Ranking Passes
# Difficulty: Easy
# Scenario: After a mock test, a teacher sorts the n marks of a small group in ascending order by hand using
# the 'bubble' method: she repeatedly walks along the list, swapping any two neighbouring marks that are in
# the wrong order. She wants to know how many walks (passes) were actually needed, meaning passes in
# which at least one swap happened, to judge how disordered the list was.
# Problem statement: Implement bubble sort on the n marks (ascending). In each pass compare
# neighbouring pairs from the left end; swap a pair only if the left mark is strictly greater than the right one.
# Print the sorted marks on the first line and, on the second line, the number of productive passes, i.e. passes
# in which at least one swap was performed. Built-in sorting is not allowed.
# Input format:
# Line 1: integer n.
# Line 2: n space-separated integers, the marks.
# Output format:
# Line 1: the sorted marks separated by spaces.
# Line 2: the number of passes that performed at least one swap.
# Constraints:
# • 1 ≤ n ≤ 2000
# • 0 ≤ mark ≤ 100
# Sample input:
# 5
# 5 1 4 2 8
# Sample output:
# 1 2 4 5 8
# 2


n = int(input().strip())
marks = list(map(int, input().strip().split()))

productive_passes = 0

for i in range(n - 1):
    swapped = False

    for j in range(n - 1 - i):
        if marks[j] > marks[j + 1]:
            temp = marks[j]
            marks[j] = marks[j + 1]
            marks[j + 1] = temp
            swapped = True

    if swapped:
        productive_passes += 1
    else:
        break

for i in range(n):
    if i > 0:
        print(" ", end="")
    print(marks[i], end="")

print()
print(productive_passes)