class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
class Solution:
	def hasCycle(self, head: ListNode):
		slow, fast = head, head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				return True
		return False

head = ListNode(20)

# Inserting Node in Linked List
head.next = ListNode(4)
head.next.next = ListNode(5)
head.next.next.next = ListNode(10)

# Just to make a cycle
head.next.next.next.next = head
print(Solution().hasCycle(head))