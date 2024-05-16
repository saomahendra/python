class Solution:
	def missingNum(self, nums):
		missing = len(nums)
		for n in range(len(nums)):
			missing = missing ^ nums[n] ^ n
		return missing
print(Solution().missingNum([3,0,1]))