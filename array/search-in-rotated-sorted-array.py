class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r-l) // 2
            if target == nums[m]:
                return  m
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return  -1

print(Solution().search([4,5,6,7,0,1,2], 0))
#print(Solution().search([4,5,6,7,0,1,2], 0))
