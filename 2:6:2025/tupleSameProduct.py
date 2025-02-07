
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # count = 0
        # nums.sort()
        # if len(nums) < 4: 
        #     return 0
        
        # p1,p2 = 0, len(nums)-1
        # c1, c2 = 1,len(nums)-2
        
        # while c1 < c2 and p1< p2:
        #     # print(f"{p1} {p2} {c1} {c2}")
        #     if nums[p1]*nums[p2] == nums[c1]*nums[c2]:
        #         count += 8
        #         p1 += 1
        #         c1 += 1
        #     if nums[p1]*nums[p2] > nums[c1]*nums[c2]:
        #         p1 += 1
        #         c1 += 1
        #     if nums[p1]*nums[p2] < nums[c1]*nums[c2]:
        #         p2 -= 1
        #         c2 -= 1
                
        # return count

        product_map = defaultdict(int)
        n = len(nums)

        # go through all the pairs and increase the corresponding product freq
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_map[product] += 1

        count = 0
        # Compute valid tuples
        for freq in product_map.values():
            if freq > 1:
                count += freq * 8  
                

        return count
solution = Solution()
        
# nums = [2,3,4,6]
# print(solution.tupleSameProduct(nums))


# nums = [1,2,4,5,10]
# print(solution.tupleSameProduct(nums))
        
nums = [2,3,4,6,8,12]
print(solution.tupleSameProduct(nums))