# https://leetcode.com/problems/add-two-numbers/

from __future__ import annotations

class ListNode:
    def __init__(self, val=0, next: ListNode | None = None):
        self.val = val
        self.next = next

    def __eq__(self, other: ListNode) -> bool:
        return self.val == other.val and self.next == other.next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode:
        ans_root = ListNode()
        current_ans = ans_root

        while True:
            if l1:
                current_ans.val += l1.val
                l1 = l1.next
            if l2:
                current_ans.val += l2.val
                l2 = l2.next
            
            remainder, current_ans.val = divmod(current_ans.val, 10)

            if l1 or l2 or remainder:
                current_ans.next = ListNode(remainder)
                current_ans = current_ans.next
            else:
                return ans_root

# Test Cases

def test_addTwoNumbers():
    s = Solution()
    assert s.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))) == ListNode(7, ListNode(0, ListNode(8)))
    assert s.addTwoNumbers(ListNode(0), ListNode(0)) == ListNode(0)
    assert s.addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9, ListNode(9))))) == ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))))))
