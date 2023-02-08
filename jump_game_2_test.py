# https://leetcode.com/problems/jump-game-ii/
# Still working on this one, there is almost certainly a more optimal solution.

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        visited[0] = True

        queue = {0}
        queue_buffer = set()
        current_jumps = 0

        try:
            while not visited[-1]:
                for cur_loc in queue:
                    for next_loc in range(cur_loc + 1, 1 + cur_loc + nums[cur_loc]):
                        if not visited[next_loc]:
                            visited[next_loc] = True
                            queue_buffer.add(next_loc)
                queue, queue_buffer = queue_buffer, queue
                queue_buffer.clear()
                current_jumps += 1
        except IndexError:
            return current_jumps + 1

        return current_jumps

# Test Cases

def test_jump():
    s = Solution()
    assert s.jump([2,3,1,1,4]) == 2
    assert s.jump([2,3,0,1,4]) == 2
    assert s.jump([0]) == 0
    assert s.jump([1,2]) == 1
    assert s.jump([1,1,1,1]) == 3

if __name__ == "__main__":
    test_jump()
