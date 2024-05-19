from typing import List


class Solution:
	def houseRobber(self, nums: List[int]) -> int:
		rob1, rob2 = 0,0
		for n in nums:
			tmp = max(n+rob1, rob2)
			rob1 = rob2
			rob2 = tmp
		return rob2

print((Solution().houseRobber([1,2,3,1])))