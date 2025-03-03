
from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        p1, p2 = 0,0
        result = []
        while p1 < len(nums1) or p2 < len(nums2): 
            if p1 >= len(nums1): 
                additional = nums2[len(nums1):]
                # print("hi")
                print(additional)
                result.extend(additional)
                break
            elif p2 >= len(nums2): 
                additional = nums1[len(nums2):]
                # print("hi")
                print(additional)
                result.extend(additional)
                break
            elif nums1[p1][0] < nums2[p2][0]:
                result.append([nums1[p1][0], nums1[p1][1]])
                p1+= 1
            elif nums1[p1][0] > nums2[p2][0]:
                result.append([nums2[p2][0], nums2[p2][1]])
                p2 += 1
            else: 
                result.append([nums1[p1][0], nums1[p1][1]+nums2[p2][1]])
                p1 += 1
                p2 += 1
            # print(f"{p1} {p2}")
        return result
    
solution = Solution()


nums1 = [[148,597],[165,623],[306,359],[349,566],[403,646],[420,381],[566,543],[730,209],[757,875],[788,208],[932,695]]
nums2 = [[74,669],[87,399],[89,165],[99,749],[122,401],[138,16],[144,714],[148,206],[177,948],[211,653],[285,775],[309,289],[349,396],[386,831],[403,318],[405,119],[420,153],[468,433],[504,101],[566,128],[603,688],[618,628],[622,586],[641,46],[653,922],[672,772],[691,823],[693,900],[756,878],[757,952],[770,795],[806,118],[813,88],[919,501],[935,253],[982,385]]
print(solution.mergeArrays(nums1, nums2))
                
nums1 = [[2,4],[3,6],[5,5]]
nums2 = [[1,3],[4,3]]
print(solution.mergeArrays(nums1, nums2))
