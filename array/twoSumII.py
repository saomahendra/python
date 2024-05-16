class Solution:
	def findTwoSum(self, nums, target):
		l, r = 0, len(nums) - 1
		while l < r:
			curSum = nums[l] + nums[r]
			if curSum > target:
				r = r - 1
			elif curSum < target:
				l = l + 1
			else:
				return [l+1, r +1]
		return []
print(Solution().findTwoSum([1,3,4,5,7,10,11], 9))


