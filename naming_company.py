# https://leetcode.com/problems/naming-a-company/

from typing import List
from collections import defaultdict
from itertools import combinations

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        first_letters = defaultdict(set)
        total = 0

        for idea in ideas:
            first_letters[idea[0]].add(idea[1:])

        for a, b in combinations(first_letters.values(), 2):
            intersect = len(a & b)
            total += (intersect - len(a)) * (intersect - len(b)) * 2

        return total

# Test Cases

def test_distinctNames():
    s = Solution()
    assert s.distinctNames(["coffee","donuts","time","toffee"]) == 6
    assert s.distinctNames(["lack","back"]) == 0

if __name__ == "__main__":
    test_distinctNames()
