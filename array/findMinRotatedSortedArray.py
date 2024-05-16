class Solution:
	def findMin(self, nums):
		l = 0
		r = len(nums) - 1
		res = nums[0]
		while l <= r:
			if nums[l] < nums[r]:
				res = min(res, nums[l])
				break
			m = l + (r - l) // 2
			res = min(res, nums[m])
			if nums[m] >= nums[l]:
				l = m + 1
			else:
				r = m - 1
		return res
print(Solution().findMin([3,4,5,1,2]))
#Source https://www.youtube.com/watch?v=nIVW4P8b1VA&ab_channel=NeetCode