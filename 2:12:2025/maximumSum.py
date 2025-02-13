

from typing import List


class Solution:
    
    def calculateSum(self, num):
        sum = 0
        while num > 0:
            digit = num%10
            sum += digit
            num = num // 10
        return sum
    
    
    def maximumSum(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        freq = {}
        sum = 0
        max_sum = 0
        for num in nums:
            # print(num)
            # print(self.calculateSum(num))
            if self.calculateSum(num) in freq:
                # print(freq[self.calculateSum(num)])
                max_sum = max(max_sum, num + freq[self.calculateSum(num)])
            else: 
                freq[self.calculateSum(num)] = num
            # print(freq)
        return max_sum
    
solution = Solution()

# print(solution.calculateSum(345))

nums = [18,43,36,13,7]
print(solution.maximumSum(nums))