# https://leetcode.com/problems/fruit-into-baskets/

from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits)<=2:
            return len(fruits)

        maximum = 0
        current_baskets_length = 0
        consecutive_fruit = None
        consecutive_fruit_count = 0

        current_fruits = set()

        for current_fruit in fruits:
            if current_fruit not in current_fruits:
                current_fruits = {consecutive_fruit, current_fruit}
                maximum = max(current_baskets_length, maximum)
                current_baskets_length = consecutive_fruit_count + 1
            else:
                # Doesn't matter if below line adds to set again, can't hold duplicate objects
                current_fruits.add(current_fruit)
                current_baskets_length += 1

            if current_fruit != consecutive_fruit:
                consecutive_fruit = current_fruit
                consecutive_fruit_count = 1
            else:
                consecutive_fruit_count += 1

        return max(current_baskets_length, maximum)

# Test Cases

def test_totalFruit():
    s = Solution()
    assert s.totalFruit([1,2,1]) == 3
    assert s.totalFruit([0,1,2,2]) == 3
    assert s.totalFruit([1,2,3,2,2]) == 4
    assert s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]) == 5
    assert s.totalFruit([1,0,1,4,1,4,1,2,3]) == 5
    assert s.totalFruit([0,1,6,6,4,4,6]) == 5

if __name__ == "__main__":
    test_totalFruit()