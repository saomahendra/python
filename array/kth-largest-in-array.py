def kthLargest(nums, k):
	nums.sort()
	return nums[len(nums)-k]

print(kthLargest([36,28,9,45],2))