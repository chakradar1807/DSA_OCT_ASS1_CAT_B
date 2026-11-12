# Title: Plagiarism Pattern Scanner
# Difficulty: Medium
# Scenario: A plagiarism checker looks for 'scrambled copies' of a short keyword inside a long document: a
# stretch of text that uses exactly the same letters as the keyword, in any order. It needs the starting position of
# every such stretch.
# Problem statement: Given a text s and a keyword p (both lowercase English letters), print every index i (0-
# based, increasing) such that the substring s[i .. i+|p|−1] is an anagram of p, i.e. has the same multiset of
# letters. Print the word None if there is no such index. Overlapping occurrences are all reported.
# Input format:
# Line 1: the string s.
# Line 2: the string p.
# Output format:
# One line with the indices separated by single spaces, or None.
# Constraints:
# • 1 ≤ |s|, |p| ≤ 10^5
# • Only lowercase letters a–z
# • Counter, sorted() and slicing in the loop are not allowed
# Sample input:
# cbaebabacd
# abc
# Sample output:
# 0 6

s = input().strip()
p = input().strip()

n = len(s)
m = len(p)

if m > n:
    print("None")

else:
    pattern = [0] * 26
    window = [0] * 26

    for i in range(m):
        pattern[ord(p[i]) - ord('a')] += 1
        window[ord(s[i]) - ord('a')] += 1

    found = False

    for i in range(n - m + 1):

        if pattern == window:
            if found:
                print(" ", end="")

            print(i, end="")
            found = True

        if i < n - m:
            old_index = ord(s[i]) - ord('a')
            new_index = ord(s[i + m]) - ord('a')

            window[old_index] -= 1
            window[new_index] += 1

    if not found:
        print("None")
    else:
        print()