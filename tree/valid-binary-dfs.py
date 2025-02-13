class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def validBST(self, node):
		return self.validBSTHelper(node, float("-inf"), float("inf"))

	def validBSTHelper(self, node, left, right):
		if not node:
			return True
		if not (left < node.val < right):
			return False
		return (self.validBSTHelper(node.left, left, node.val) and
		self.validBSTHelper(node.right, node.val, right))

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
print(Solution().validBST(root))

#  5
#  /\
# 3  7