# Title: Missing Roll Numbers
# Difficulty: Medium
# Scenario: A class has n students with roll numbers 1 to n. The attendance sheet has exactly n entries, but
# because of copy-paste mistakes some roll numbers were written more than once, so some students are not
# on the sheet at all. The teacher wants the list of roll numbers that are missing from the sheet.
# Problem statement: Given n and an array of n integers, each between 1 and n inclusive, print all integers in
# the range 1..n that do not appear in the array, in increasing order, separated by single spaces. If every roll
# number appears, print the word None. The array may be modified; try to use no extra array.
# Input format:
# Line 1: integer n.
# Line 2: n space-separated integers, the roll numbers on the sheet.
# Output format:
# One line containing the missing roll numbers in increasing order separated by spaces, or None.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 1 ≤ entry ≤ n
# Sample input:
# 8
# 4 3 2 7 8 2 3 1
# Sample output:
# 5 6

n = int(input().strip())
roll_numbers = list(map(int, input().split()))

for i in range(n):
    index = abs(roll_numbers[i]) - 1

    if roll_numbers[index] > 0:
        roll_numbers[index] = -roll_numbers[index]

found = False

for i in range(n):
    if roll_numbers[i] > 0:
        if found:
            print(" ", end="")

        print(i + 1, end="")
        found = True

if not found:
    print("None")
else:
    print()