# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

from itertools import pairwise
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traverse(node):
    if node is None:
        return
    yield from inorder_traverse(node.left)
    yield node.val
    yield from inorder_traverse(node.right)

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        return min(b - a for a, b in pairwise(inorder_traverse(root)))

# Test Cases

def test_minDiffInBST():
    s = Solution()
    assert s.minDiffInBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))) == 1
    assert s.minDiffInBST(TreeNode(1, None, TreeNode(3, TreeNode(2)))) == 1

if __name__ == "__main__":
    test_minDiffInBST()
