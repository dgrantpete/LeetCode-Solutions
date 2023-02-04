# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = set(s1)


# Test Cases

def test_checkInclusion():
    s = Solution()
    assert s.checkInclusion("ab", "eidbaooo") == True
    assert s.checkInclusion("ab", "eidboaoo") == False