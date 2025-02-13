

class Solution:
    
    def removeOccurrences(self, s: str, part: str) -> str:
        stack_match = []
        for i in range(len(s)):
            
            stack_match.append(s[i])
            if s[i] == part[len(part)-1]:
                for part_token in reversed(part):
                    next_char = stack_match.pop()
                    if part_token != next_char:
                        stack_match.append(next_char)
                        break
                    else: 
                        continue
        new_s = ""
        while stack_match:
            new_s = stack_match.pop() + new_s
        
        return new_s
            
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []  # Stack to build the string dynamically
        part_len = len(part)  # Length of the part substring
        
        for char in s:
            stack.append(char)  # Add character to the stack
            
            # Checks if the end of the stack matches 'part'
            if len(stack) >= part_len and "".join(stack[-part_len:]) == part:
                # If a match is found, remove the last `part_len` characters
                
                # would this take more time because of slice?
                del stack[-part_len:]
        
        return "".join(stack)

    
solution = Solution()

s="daabcbaabcbc"
part = "abc"
print(solution.removeOccurrences(s,part))

s = "axxxxyyyyb"
part = "xy"
print(solution.removeOccurrences(s,part))

s = "gjzgbpggjzgbpgsvpwdk"
part = "gjzgbpg"
print(solution.removeOccurrences(s,part))