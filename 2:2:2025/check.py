from typing import List
# A[i] == B[(i+x) % A.length]
class Solution:
    def check(self, nums: List[int]) -> bool:
        a_list = [0]*len(nums)
        
        # go the rotated array. try to make the original array 
            # by shifting to left
        for x in range(len(nums)):
            
            # go the rotated array. Check if 
            for i in range(len(nums)):
                a_list[i] = nums[(i+x)%len(a_list)]
                
            if a_list == sorted(a_list):
                return True
            
        return False
        
solution = Solution()


# a faster intuition is to find where the decrease happened 
# (nums[i - 1] > nums[i]), 
# then check if each side is sorted

# def checkSorted: goes through the array and 
# checks if the next index is bigger than curr index

# def check: keep the index where the rotation might have happened in a var
# once you find it, check and see if each side is sorted. 
# if k=0, then its already sorted
# if k = wtv, then check nums[k:] (afterwards) + nums[:k] (before) are sorted. 


nums = [3,4,5,1,2]
print(solution.check(nums))

nums = [2,1,3,4]
print(solution.check(nums))

nums = [1,2,3]
print(solution.check(nums))
