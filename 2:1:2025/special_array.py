from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        
        
        for i in range(len(nums)-1):
            if nums[i]%2 == nums[i+1]%2:
                return False
        return True

# Example cases
solution = Solution()


nums = [1]
print(solution.isArraySpecial(nums))

nums = [2,1,4]
print(solution.isArraySpecial(nums))

nums = [4,3,1,6]
print(solution.isArraySpecial(nums))
