from bisect import bisect_right
from typing import List
import timeit

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words_sorted = [[] for _ in range(30)]
        for word in words:
            words_sorted[len(word)].append(word)

        unique_words = set()

        word_lengths = [i for i, lst in enumerate(words_sorted) if lst]

        for word_length in word_lengths:
            if word_length < word_lengths[0] * 2:
                unique_words.update(words_sorted[word_length])
            else:
                break
        
        concatenated_words = []
        print(list(set(words) - unique_words))
        return list(set(words) - unique_words)
        
        
def test_cases(s: Solution):
    # Torture test
    assert s.findAllConcatenatedWordsInADict(["bats", "cats", "cat", "bat", "ba", "bats", "ts"]) == ["bats"]
    assert s.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]) == ["catsdogcats","dogcatsdog","ratcatdogcat"]

test_cases(Solution())

# Time test "test_cases" and print out time it takes to run
# def time_test(test_cases):
#     s = Solution()
#     time = min(timeit.repeat(lambda: test_cases(s), number=50, repeat=10))
#     print(f"Time: {time:.3f} seconds")

# time_test(test_cases)