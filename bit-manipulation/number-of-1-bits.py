class Solution:
	def countOnes(self, n):
		res = 0
		while n > 0:
			res = res + n % 2
			n = n >> 1
		return res
print(Solution().countOnes(8))