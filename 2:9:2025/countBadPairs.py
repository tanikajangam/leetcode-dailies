
from typing import List


class Solution:
    
    def countBadPairs(self, nums: List[int]) -> int:
        goodPairs = 0
        freq = {}
        for i in range(len(nums)):
            diff = nums[i] - i  
            if diff in freq:
                goodPairs += freq[diff]
                freq[diff] += 1
            else:
                freq[diff] = 1
        
        return (len(nums)*(len(nums)-1))//2-goodPairs
            
solution = Solution()


nums = [4,1,3,3]
print(solution.countBadPairs(nums))

nums = [1,2,3,4,5]
print(solution.countBadPairs(nums))