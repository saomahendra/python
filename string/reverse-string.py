def reverseStr(str):
	l, r = 0, len(str) - 1
	while (l<r):
		str[l], str[r] = str[r], str[l]
		l,r = l+1, r-1
	return str

def reverseStr2(str2): #time O(n) and space O(1)
	str = list(str2) # Converting string to char array
	l, r = 0, len(str) - 1
	while (l<r):
		str[l], str[r] = str[r], str[l]
		l,r = l+1, r-1
	return str
#using stack
def reverseStrUsingStack(str): #time O(n) space O(n)
	#str = list(str3)
	stack = []
	for s in range(len(str)):
		stack.append(str[s])
	i = 0
	while stack:
		str[i] = stack.pop()
		i+=1
	return str
#using recursion
def revesreUsingRecur(str):
	def reverse(l,r):
		if l < r:
			str[l], str[r] = str[r], str[l]
			reverse(l+1, r-1)
	reverse(0, len(str)-1)
	return str


print(revesreUsingRecur(["h","e", "l"]))