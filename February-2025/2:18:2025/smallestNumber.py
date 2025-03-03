


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        inc = [] #list for increasing indicies
        dec = []#list for decreasing indicies
        result = [] #resultant set
        taken = set() #set that makes sure no value is used more than once
        
        for i in range(len(pattern)):
            if pattern[i] == 'I':
                # add to increasing list if pattern is I
                inc.append(i)
                    
            else:
                
                # add to dec list if patter is D
                dec.append(i)  
            
        # pointers for inc set and dec set
        p_1, p_2 = 0,0
        # starting value
        val = 1
        
        while p_1 < len(inc) and p_2 < len(inc):
            # if the next number has to be increasing
            while inc[p_1] < dec[p_2] and p_1 < len(inc): 
                while val in taken: #choose the next available value
                    val += 1
                result.append(val)
                p_1 += 1
            if dec[p_2] < inc[p_1]: 
                
                starting_indx = p_2
            # if the next number has to be decreasing
                while dec[p_2] < inc[p_1] and p_2 < len(inc):
                    while val in taken: #choose the next available value
                        val += 1
                    result.append(val)
                    p_2 += 1
                # reverse our local list so that it's decreasing
                reverse = sorted(result[starting_indx:p_2+1], reverse = True)
                result[starting_indx:p_2+1] = reverse
        print(result)
        
        
        # stack based approach: pop numbers if they are I, 
        # otherwise keep adding to the stack
        # stack =  = []
        # result = []
        # num = 1  # Start numbering from 1
        
        # for i in range(len(pattern) + 1):  
        #     stack.append(str(num))  # Always push the next number
            
        #     # If it's the end or we encounter an 'I', process the stack
        #     if i == len(pattern) or pattern[i] == 'I':
        #         while stack:
        #             result.append(stack.pop())
            
        #     num += 1  # Increment for the next number
        
        # return "".join(result)
                
    
solution = Solution()    
pattern = "IIIDIDDD"

print(solution.smallestNumber(pattern))
