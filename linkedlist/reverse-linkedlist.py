from typing import Optional
class ListNode:

     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

     def __repr__(self):
         return f"({self.val}, {self.next})"

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
print(Solution().reverseList(node))

