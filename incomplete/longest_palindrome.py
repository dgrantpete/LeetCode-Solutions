from math import floor, ceil

def is_palindrome(string, left = 0, right = None):
    if right is None:
        right = len(string) - 1
    midpoint = (left + right) / 2
    midleft, midright = floor(midpoint), ceil(midpoint)

    return string[midleft:left:-1] == string[midright:right]

def longestPalindrome(s: str) -> str:
    s_rev = reversed(s)
    for i, start in enumerate(s):
        for j, end in enumerate(s_rev, -len(s) + 1):
            if start == end and is_palindrome(s, i, abs(j)):
                return s[i:abs(j) + 1]
            break

    return ""

print(longestPalindrome("racecar"))
print(longestPalindrome("cbbd"))