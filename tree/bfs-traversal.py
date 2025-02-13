# Definition for a binary tree node.
import collections
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def levelOrder(self, root):
		res = []
		q = collections.deque()
		q.append(root)
		while q:
			qLen = len(q)
			level = []

			for i in range(qLen):
				node = q.popleft()
				if node:
					level.append(node.val)
					q.append(node.left)
					q.append(node.right)
			if level:
				res.append(level)

		return res

	def bfsTraversal(self, root):
		q = collections.deque()
		q.append(root)
		while q:
			node = q.popleft()
			print(node.val, end=" ")
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(Solution().bfsTraversal(root))


#	 5
#   /\
#  3  7
