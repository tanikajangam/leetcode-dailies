

from collections import deque


class Solution:
    def coloredCells(self, n: int) -> int:
        rows, cols = n*2-1,n*2-1
        visited = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        count = 1
        def traverse(i, j, count, n):
            queue = deque([(i, j)])
            while queue and n>0:
                curr_i, curr_j = queue.popleft()
                print(f"i:{curr_i} j:{curr_j}")
                print(curr_j)
                if (curr_i, curr_j) not in visited:
                    visited.add((curr_i, curr_j))
                    # Traverse neighbors.
                    for direction in directions:
                        next_i, next_j = curr_i + direction[0], curr_j + direction[1]
                        if 0 <= next_i < rows and 0 <= next_j < cols:
                            count += 1
                            queue.append((bnext_i, next_j))  
                    n -= 1
                        

        traverse(n, n, count, n)

        return count
    
solution = Solution()

print(solution.coloredCells(n=4))
# solution.coloredCells(n=1)