from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors_freq = {}
        balls = [0]*(limit+1)
        output = []

        for i in range(len(queries)):
            
            # print(queries[i][0])
            # print(queries[i][1])
            if balls[queries[i][0]] != 0:
                colors_freq[balls[queries[i][0]]] -= 1
                if colors_freq[balls[queries[i][0]]] == 0:
                    del colors_freq[balls[queries[i][0]]]

                
            balls[queries[i][0]] = queries[i][1]
            if queries[i][1] not in colors_freq:
                colors_freq[queries[i][1]] = 1
            else: 
                colors_freq[queries[i][1]] += 1
            # print(colors_freq)
            output.append(len(colors_freq))
        # count = 0
        return output
    
    
    # Better solution: 
    # def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
    #     ball_colors = {}  # Tracks the current color of each ball
    #     color_count = {}  # Tracks how many balls have each color
    #     distinct_colors = 0  # Tracks number of distinct colors
    #     result = []

    #     for ball, new_color in queries:
    
    
    #         if ball in ball_colors:  
    #             old_color = ball_colors[ball]
    
    #             color_count[old_color] -= 1
    
    #             if color_count[old_color] == 0:
    #                 distinct_colors -= 1  # Remove from distinct colors if no ball has it anymore

    #         # Assign new color
    #         ball_colors[ball] = new_color
    #         if new_color not in color_count:
    #             color_count[new_color] = 0
    #             distinct_colors += 1  # New distinct color added
    #         color_count[new_color] += 1

    #         result.append(distinct_colors)

    #     return result
solution = Solution()



limit = 4
queries = [[1,4],[2,5],[1,3],[3,4]]
print(solution.queryResults(limit, queries))

limit = 4
queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
print(solution.queryResults(limit, queries))


# 