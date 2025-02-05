


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        wrong_letters = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                wrong_letters.append(i)
        # print(wrong_letters)
    
        
        if wrong_letters: 
            if len(wrong_letters) != 2: #has to equal 2
                return False
            first_wrong = wrong_letters[0]
            second_wrong = wrong_letters[1]
            # print("hi")
            # print(s1[:first_wrong])
            # print(s1[second_wrong])
            new_s = s1[:first_wrong]+""+s1[second_wrong]+s1[first_wrong+1:second_wrong]+s1[first_wrong]+s1[second_wrong+1:]
                
            # print(new_s)
            if new_s != s2:
                return False
        return True


solution = Solution()

s1 = "bank"
s2 = "kanb"
print(solution.areAlmostEqual(s1, s2))

s1 = "attack"
s2 = "defend"
print(solution.areAlmostEqual(s1, s2))

s1 = "kelb"
s2 = "kelb"
print(solution.areAlmostEqual(s1, s2))