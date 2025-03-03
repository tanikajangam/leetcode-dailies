


class Solution:

    def partition(first_half, second_half):
        
        if first_half < 10 and second_half < 10 and first_half + second_half == i: 
            return i
        else: 
            return partition(first_half[:len(first_half/2]) + second_half[second_half:]) 
            
        

        
    def punishmentNumber(self, n: int) -> int:
        sum = 0
        for i in range(n):
            square = i*i
            first_half = s.split()
            sum +=partition()
        return sum