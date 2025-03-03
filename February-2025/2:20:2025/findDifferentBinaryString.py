

from inspect import stack
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        bin_len = len(nums[0])
        num_stack = set()
        for i in range(len(nums)):
            val = int(nums[i], 2)
            num_stack.add(val)

        j = 0
        max_num = 2**bin_len
        while j < max_num: 
            if j not in num_stack:
                return int(j, 2)
        return None
    
    
        # n = len(nums)
        # num_set = set(nums)  # Store existing numbers for quick lookup
        
        # # Generate a unique binary string using diagonalization
        # candidate = ''.join('1' if nums[i][i] == '0' else '0' for i in range(n))
        
        # # If this candidate is not in the set return it
        # if candidate not in num_set:
        #     return candidate
        
        # # Otherwise, iterate through all possibilities
        # for i in range(2 ** n):
        #     binary_str = format(i, f'0{n}b')
        #     if binary_str not in num_set:
        #         return binary_str
        
        # return ""  # Should never be reached