# https://leetcode.com/problems/as-far-from-land-as-possible/

from typing import List
from itertools import count

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        vectors = ((0, -1), (-1, 0), (0, 1), (1, 0))

        height, width = len(grid), len(grid[0])

        queue = [(i, j) for i, sublist in enumerate(grid) for j, item in enumerate(sublist) if item]
        queue_buffer = []

        if len(queue) != height * width and queue:
            for i in count():
                for y, x in queue:
                    for dy, dx in vectors:
                        x_sum, y_sum = x + dx, y + dy
                        if 0 <= x_sum < width and 0 <= y_sum < height and not grid[y_sum][x_sum]:
                            grid[y_sum][x_sum] = 1
                            queue_buffer.append((y_sum, x_sum))
                if not queue_buffer:
                    return i
                queue, queue_buffer = queue_buffer, queue
                queue_buffer.clear()

        return -1

# Test Cases

def test_maxDistance():
    s = Solution()
    assert s.maxDistance([[1,0,1],[0,0,0],[1,0,1]]) == 2
    assert s.maxDistance([[1,0,0],[0,0,0],[0,0,0]]) == 4

if __name__ == "__main__":
    test_maxDistance()
