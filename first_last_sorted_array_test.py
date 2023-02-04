# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List

def bin_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = bin_search(nums, target)

        if index == -1:
            return [-1, -1]
        else:
            return [index - next((i for i, x in enumerate(nums[index::-1], -1) if x != target), index), next((i for i, x in enumerate(nums[index:], index - 1) if x != target), len(nums) - 1)]
            
# Test cases

def test_searchRange():
    s = Solution()
    assert s.searchRange([5,7,7,8,8,10], 8) == [3, 4]
    assert s.searchRange([5,7,7,8,8,10], 6) == [-1, -1]
    assert s.searchRange([], 0) == [-1, -1]
