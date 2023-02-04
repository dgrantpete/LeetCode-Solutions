# https://leetcode.com/problems/snakes-and-ladders/

from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        # Flattens the board, reversing every other row in a single list comprehension.
        flattened_board = [column for i, row in enumerate(reversed(board)) for column in (row if i % 2 == 0 else reversed(row))]
        flattened_board = [i - 1 if i != -1 else -1 for i in flattened_board]

        min_steps_to_loc = [float('inf')] * len(flattened_board)
        min_steps_to_loc[0] = 0

        queue = deque([0])
        current_steps = 0

        while queue:
            current_loc = queue.pop()
            current_steps = min_steps_to_loc[current_loc]
            if current_loc + 7 >= len(flattened_board):
                return current_steps + 1

            for roll in range(1, 7):
                next_loc = current_loc + roll
                
                if flattened_board[next_loc] != -1:
                    next_loc = flattened_board[next_loc]

                    if next_loc >= len(flattened_board) - 1:
                        return current_steps + 1

                if min_steps_to_loc[next_loc] > current_steps + 1:
                    min_steps_to_loc[next_loc] = current_steps + 1
                    queue.appendleft(next_loc)

        return -1

# Test cases

def test_snakesAndLadders():
    s = Solution()
    assert s.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]) == 4
    assert s.snakesAndLadders([[-1,-1],[-1,3]]) == 1
