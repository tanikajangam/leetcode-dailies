# You are given an array of integers nums. 
# Return the length of the longest subarray of nums which is either s
# trictly increasing or strictly decreasing .

from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        low,high = 0,0
        max_len = 1
        isIncreasing = True
        isDecreasing = True

        while high < len(nums)-1:
            
            if nums[high] < nums[high+1] and isIncreasing:
                high += 1
                isIncreasing = True
                isDecreasing = False
            elif nums[high] > nums[high+1] and isDecreasing:
                high += 1
                isIncreasing = False
                isDecreasing = True
            elif nums[high] == nums[high+1]:
                high += 1
                low = high
                isIncreasing = True
                isDecreasing = True
            else: 
                low = high
                isIncreasing = True
                isDecreasing = True


            max_len = max(max_len, high-low+1)
        return max_len
    
    
    # an alternative solution that I found is to:
    # go through array, and if index is greater than previous, increase temp_count and set maxlen
    # go through array again, and if index is less than previous, increase temp_count and set maxlen
    # return max. Its easier, but I'm glad I got to practice sliding window LOL
    # O(n), which is same as this time complexity
            
solution = Solution()

nums = [1,4,3,3,2]
print(solution.longestMonotonicSubarray(nums))

nums = [3,3,3,3]
print(solution.longestMonotonicSubarray(nums))

nums = [3,2,1]
print(solution.longestMonotonicSubarray(nums))