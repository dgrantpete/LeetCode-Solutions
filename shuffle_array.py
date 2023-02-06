# https://leetcode.com/problems/shuffle-the-array/

from itertools import islice, chain
from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [x for x in chain(*zip(islice(nums, None, n), islice(nums, n, None)))]

# Test Cases

def test_shuffle():
    s = Solution()
    assert s.shuffle([2,5,1,3,4,7], 3) == [2,3,5,4,1,7]
    assert s.shuffle([1,2,3,4,4,3,2,1], 4) == [1,4,2,3,3,2,4,1]
    assert s.shuffle([1,1,2,2], 2) == [1,2,1,2]

if __name__ == "__main__":
    test_shuffle()
