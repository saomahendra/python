from collections import Counter


def isAnagram(str1, str2):
	if len(str1) != len(str2):
		return False
	couterStr1, couterStr2 = {}, {}
	for i in range(len(str1)):
		#print(str1[i], str2[i])
		couterStr1[str1[i]] = 1 + couterStr1.get(str1[i],0)
		couterStr2[str2[i]] = 1 + couterStr2.get(str2[i], 0)
	for c in couterStr1:
		#print(i , couterStr1[i])
		if couterStr1[c] != couterStr2.get(c, 0):
			return False
		#print(couterStr1[i])
	return True
def isAnagram2(str1, str2):
	return Counter(str1) == Counter(str2)

def isAnagram3(str1, str2):
	return sorted(str1) == sorted(str2)

print(isAnagram2("abcda", "dcbaa"))