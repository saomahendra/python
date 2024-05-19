from typing import List


class Solution:
	def rob(self, nums: List[int]) -> int:
		return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
	def helper(self, nums: List[int]) -> int:
		rob1, rob2 = 0, 0
		for n in nums:
			new_rob = max(n+rob1, rob2)
			rob1 = rob2
			rob2 = new_rob
		return rob2
print(Solution().rob([2,3,2]))
