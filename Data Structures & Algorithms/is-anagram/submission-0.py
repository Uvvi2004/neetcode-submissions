class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one = {}
        two = {}

        for i in s:
            if i in one:
                one[i] += 1
            else:
                one[i] = 1
        
        for j in t:
            if j in two:
                two[j] += 1
            else:
                two[j] = 1
        
        if one == two:
            return True
        else:
            return False

