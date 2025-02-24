

from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = [[]]
        isopen = []*len(graph)*True
        for edge in edges:
            graph[edge[0]].append(edge[1])
            
        while bob != 0: 
            isopen[bob] = False
            
            
        return None
    
    
solution = Solution()


edges = [[0,1],[1,2],[1,3],[3,4]]
bob = 3
amount = [-2,4,2,-4,6]
print(solution.mostProfitablePath(edges, bob, amount))