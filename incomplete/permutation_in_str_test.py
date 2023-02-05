# This implementation seems to be the naive case, I'm certain there is a faster way. Trying to work out what it would be.

# https://leetcode.com/problems/permutation-in-string/

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        letters = Counter(s1)

        possible_start_locs = []

        current_trues = 0
        for i, start_loc in enumerate(reversed(s2), start=1):
            if start_loc in letters:
                current_trues += 1
                if current_trues >= len(s1):
                    possible_start_locs.append(len(s2) - i)
            else:
                current_trues = 0

        return any(Counter(s2[i:i+len(s2)]) for i in possible_start_locs)

# Test Cases

def test_checkInclusion():
    s = Solution()
    assert s.checkInclusion("ab", "eidbaooo") == True
    assert s.checkInclusion("ab", "eidboaoo") == False

print(Solution().checkInclusion("ab", "eidbaooo"))