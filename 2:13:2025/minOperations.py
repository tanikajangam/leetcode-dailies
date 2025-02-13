from typing import List
import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        k_count = {}
        k_count[0] = len(nums)
        k_count[1] = 0
        operations = 0
        nums.sort()
        for num in nums:
            if num >= k:
                k_count[1] += 1
                k_count[0] -= 1
        # print(k_count)
        while k_count[0] > 0: 
            x = nums[0]
            y = nums[1]
            k_count[0] -= 2
            operations += 1
            val = min(x, y) * 2 + max(x, y) 
            # heapq.heappush(val)
            if val >= k:
                k_count[1] += 1
            else: 
                k_count[0] += 1
            nums[0] = val
            nums[1] = float('inf')
            
            nums.sort()
            # print(f"k_count = {k_count}")
            # print(nums)
            
        
        return operations
    
    
    
        #  next time, really think about what ds i need to use and try it out. 
        # converts nums into a min heap
        # heapq.heapify(nums)  # Convert nums into a min-heap
        # operations = 0
        
        # # while the smallest number is less than k
        # while nums and nums[0] < k:
        #     if len(nums) < 2:
        #         return -1  # Not enough elements to continue
            
        #     x = heapq.heappop(nums)  # Smallest element
        #     y = heapq.heappop(nums)  # Second smallest element
            
        #     new_val =m in(x, y) * 2 + max(x, y)  # Combine elements based on given rule
        #     heapq.heappush(nums, new_val)  # ad dnew value to nums
        #     operations += 1 # add 1 to operations value
        
        # return operations

solution = Solution()
nums = [2,11,10,1,3]
k=10
print(solution.minOperations(nums, k))

nums = [1,1,2,4,9]
k=20
print(solution.minOperations(nums, k))
