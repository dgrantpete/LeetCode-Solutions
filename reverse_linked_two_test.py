# https://leetcode.com/problems/reverse-linked-list-ii/

from typing import Optional
from itertools import pairwise

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __eq__(self, other):
        if isinstance(other, ListNode):
            return self.val == other.val and self.next == other.next
        return False

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node_references = []

        cur = head
        while cur is not None:
            node_references.append(cur)
            cur = cur.next

        if len(node_references) < 2:
            return head

        node_references[left-1:right] = reversed(node_references[left-1:right])

        for node, next_node in pairwise(node_references):
            node.next = next_node

        node_references[-1].next = None

        return node_references[0]

# Test Cases

def test_reverseBetween():
    s = Solution()
    assert s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4) == ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))
    assert s.reverseBetween(ListNode(3, ListNode(5)), 1, 2) == ListNode(5, ListNode(3))

if __name__ == "__main__":
    test_reverseBetween()