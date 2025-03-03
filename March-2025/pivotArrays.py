from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        larger = []
        equal = []
        
        for i in range(len(nums)):
            if nums[i] < pivot:
                smaller.append(nums[i])
            
            elif nums[i] > pivot:
                larger.append(nums[i])
            
            else:
                equal.append(nums[i])
            
        result = []
        
        result.extend(smaller)
        result.extend(equal)
        result.extend(larger)
        return result
    

solution = Solution()
nums = [9,12,5,10,14,3,10]
pivot = 10

# print(solution.pivotArray(nums, pivot))