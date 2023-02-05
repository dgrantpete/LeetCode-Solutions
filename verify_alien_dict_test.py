# https://leetcode.com/problems/verifying-an-alien-dictionary/

from itertools import pairwise
from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        values = {c: i for i, c in enumerate(order)}

        return all(
            next(
                (
                    values[a] < values[b]
                    for a, b in zip(word_a, word_b)
                    if a != b
                ),
                len(word_a) <= len(word_b)
            )
            for word_a, word_b in pairwise(words)
        )

# Test cases

def test_isAlienSorted():
    s = Solution()
    assert s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz") == True
    assert s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz") == False
    assert s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz") == False

if __name__ == "__main__":
    test_isAlienSorted()
    