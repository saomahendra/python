class Solution:
  #working in leetcode
  def max_subarray(self, nums):
    max_so_far = nums[0]
    curr_max = nums[0]
    for i in range(1, len(nums)):
      curr_max = max(nums[i], curr_max + nums[i])
      max_so_far = max(max_so_far, curr_max)
    return max_so_far

  def maxSubArray2(self, nums):
    maxSum = 0
    sum = 0
    for n in nums:
      sum += n
      if sum < 0:
        sum = 0
      else:
        maxSum = max(maxSum, sum)
    return maxSum



print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# 6

print(Solution().maxSubArray([-1, -4, 3, 8, 1]))
# 12