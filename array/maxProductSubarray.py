class Solution:
	def maxProduct(self, nums):
		res = max(nums)
		curMax, curMin = 1, 1
		for n in nums:
			if n == 0:
				curMax, curMin = 1, 1
			temp = curMax * n
			curMax = max(n * curMax, n * curMin, n)
			curMin = min(temp, n * curMin, n)
			res = max(res, curMax)
		return res
print(Solution().maxProduct([2,3,-2,4]))
#from you tube https://www.youtube.com/watch?v=lXVy6YWFcRM&ab_channel=NeetCode


