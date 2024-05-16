def containsDuplicate(nums):
	set1 = set()

	for num in nums:
		if num in set1:
			return True
		else:
			set1.add(num)
	return False
print(containsDuplicate([1,2,3,1]))