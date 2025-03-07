from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        values = set()
        
        num = set()
        for i in range(len(grid)*2):
            num.add(i+1)
        # print(f" num: {num}")
        missing = 0
        double = 0

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] not in values: 
                    values.add(grid[i][j])
                else: 
                    double = grid[i][j]
        
        
        # prist(f" values: {values}")
        difference_set = num-values
        
        for val in difference_set:
            missing = val
        return [double, missing]
    
solution = Solution()

grid = [[1,3],[2,2]]
print(solution.findMissingAndRepeatedValues(grid))

