from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        temp_count = 0
        max_count = 0
        
        for i in range(1, len(nums)):
            
            if nums[i-1] < nums[i]:
                temp_count += nums[i-1]
                max_count = max(max_count, temp_count)
            elif nums[i-1] >= nums[i]:
                temp_count += nums[i-1]
                
                max_count = max(max_count, temp_count)
                
                temp_count = 0
            
        if nums[len(nums)-1] > nums[len(nums)-2]:
                temp_count += nums[len(nums)-1]
                max_count = max(max_count, temp_count)
        else: 
            temp_count = nums[len(nums)-1] 
            max_count = max(max_count, temp_count)
            
                
        return max_count
    
    # a better way to implement this, is to initialize
    # cur to num[0] in the beginning, then do the normal check
    # to see if nums[i] < nums[i+1]. Setting it equal to 
    # nums[0] solves the problem of not counting the beginning

solution = Solution()

nums = [10,20,30,5,10,50]
print(solution.maxAscendingSum(nums))

nums = [10,20,30,40,50]
print(solution.maxAscendingSum(nums))

nums = [12,17,15,13,10,11,12]
print(solution.maxAscendingSum(nums))