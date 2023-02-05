# https://leetcode.com/problems/contains-duplicate/

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Test cases

def test_containsDuplicate():
    s = Solution()
    assert s.containsDuplicate([1,2,3,1]) == True
    assert s.containsDuplicate([1,2,3,4]) == False
    assert s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True

if __name__ == "__main__":
    test_containsDuplicate()
    