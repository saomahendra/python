class Solution:
	def longestConsecutiveSequence(self, nums):
		num_set= set(nums)
		longest = 0
		for n in nums:
			if n-1 not in num_set:
				length = 1
				while n + length in num_set:
					length+= 1
					longest = max(longest, length)
		return longest
print(Solution().longestConsecutiveSequence([0,3,7,2,5,8,4,6,0,1]))