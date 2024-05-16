class Solution:
	def sumOfTwoInt(self, a, b):
		mask = 0xffffffff
		while (mask&b) > 0:
			a,b = a^b, (a&b) << 1
		return (mask&a) if b > 0 else a

print(Solution().sumOfTwoInt(-16,20))