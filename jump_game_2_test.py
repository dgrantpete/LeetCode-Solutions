# https://leetcode.com/problems/jump-game-ii/

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        max_reach = 0
        end = 0
        for i, num in zip(range(len(nums)-1), nums):
            if (cur_dist := i + num) > max_reach:
                max_reach = cur_dist
            if i == end:
                jumps += 1
                end = max_reach
        return jumps

# Test Cases

def test_jump():
    s = Solution()
    assert s.jump([2,3,1,1,4]) == 2
    assert s.jump([2,3,0,1,4]) == 2
    assert s.jump([0]) == 0
    assert s.jump([1,2]) == 1
    assert s.jump([1,1,1,1]) == 3
    assert s.jump([2, 1]) == 1

if __name__ == "__main__":
    test_jump()
