

class Solution:
    def clearDigits(self, s: str) -> str:
        map = {}
        for i in range(1, len(s)):
            if s[i].isdigit():
                    j = i-1
                    while s[j] in map or s[j].isdigit():
                        j -= 1
                    map[j] = s[i]
        
        new_s = ""
        for i in range(len(s)-1):
            j = len(s)-i
            if s[i] not in map and s[i].isdigit() == False:
                new_s += s[i]
        return new_s


# class Solution:
#     def clearDigits(self, s: str) -> str:
#         stack = []
        
#         for char in s:
#             if char.isdigit():
#                 if stack:  # Remove the closest non-digit from the stack
#                     stack.pop()
#             else:
#                 stack.append(char)  # Add non-digit to stack
        
#         return "".join(stack)  # Construct the final string

solution = Solution()


s="abc"
print(solution.clearDigits(s))

s="cb34"
print(solution.clearDigits(s))

s="c5c"
print(solution.clearDigits(s))
