from cmath import inf
from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def isPrime(num):
            for i in range(2,num-1):
                if num%i ==0:
                    return False
            return True
        
        close = []
        difference = float(inf)
        smaller = -1
        larger = -1
        for j in range(left, right):
            if isPrime(j):
                if larger != -1: 
                    smaller = larger
                    larger = j
                    # print(f"{smaller}, {larger}")
                    if difference > larger-smaller:
                        close = [smaller, larger]
                        difference = larger-smaller
                        print(difference)
                else:
                    smaller = larger
                    larger = j
        return close


solution = Solution()

left = 10
right = 19
print(solution.closestPrimes(left, right))