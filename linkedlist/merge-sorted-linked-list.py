class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	def __repr__(self):
		return f"({self.val}, {self.next})"

class Solution:
	def mergeLinkedLists(self, list1:ListNode, list2:ListNode)-> ListNode:
		dummy = node = ListNode()
		while list1 and list2:
			if list1.val < list2.val:
				node.next = list1
				list1 = list1.next
			else:
				node.next = list2
				list2 = list2.next
			node = node.next
		node.next = list1 or list2
		return dummy.next

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

print(Solution().mergeLinkedLists(list1, list2))
