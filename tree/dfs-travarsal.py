class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def in_order_traversal(self, node):
		if node:
			self.in_order_traversal(node.left)
			print(node.val,  end=" ")
			self.in_order_traversal(node.right)

	def pre_order_traversal(self,node):
		if node:
			print(node.val, end=" ")
			self.pre_order_traversal(node.left)
			self.pre_order_traversal(node.right)

	def post_order_traversal(self, node):
		if node:
			self.post_order_traversal(node.left)
			self.post_order_traversal(node.right)
			print(node.val, end=" ")

	def iterative_in_order(root):
		stack = []
		current = root
		while stack or current:
			while current:
				stack.append(current)
				current = current.left
			current = stack.pop()
			print(current.val, end=" ")
			current = current.right

	def iterative_pre_order(root):
		if not root:
			return
		stack = [root]
		while stack:
			node = stack.pop()
			print(node.val, end=" ")
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)

	def iterative_post_order(root):
		if not root:
			return
		stack = [root]
		result = []
		while stack:
			node = stack.pop()
			result.append(node.val)
			if node.left:
				stack.append(node.left)
			if node.right:
				stack.append(node.right)
		print(" ".join(map(str, result[::-1])))


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(Solution().in_order_traversal(root))
print(Solution().pre_order_traversal(root))
print(Solution().post_order_traversal(root))