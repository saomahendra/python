class Solution:
	def largestCommonPrefix(self, strList):
		res = ""
		for i in range(len(strList[0])):
			for str in strList:
				if i == len(str) or str[i] != strList[0][i]:
					return res
			res+=strList[0][i]
		return res
print(Solution().largestCommonPrefix(["aab", "aacd", "aaef"]))