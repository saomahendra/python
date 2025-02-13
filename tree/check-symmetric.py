from collections import deque


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def is_symmetric(root):
	def is_mirror(t1, t2):
		if not t1 and not t2:  # Both nodes are None
			return True
		if not t1 or not t2:  # One node is None but not the other
			return False
		# Check if the current nodes are equal and their children are mirrors
		return (t1.val == t2.val and
				is_mirror(t1.left, t2.right) and
				is_mirror(t1.right, t2.left))

	return is_mirror(root, root) #if root else True


def is_symmetric_iterative(root):
    if not root:
        return True

    queue = deque([(root.left, root.right)])  # Initialize queue with the root's children

    while queue:
        t1, t2 = queue.popleft()

        if not t1 and not t2:
            continue  # Both nodes are None, so continue checking others
        if not t1 or not t2 or t1.val != t2.val:
            return False  # Asymmetry found

        # Enqueue the children in mirrored order
        queue.append((t1.left, t2.right))
        queue.append((t1.right, t2.left))

    return True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
print(is_symmetric(root))
print(is_symmetric_iterative(root))