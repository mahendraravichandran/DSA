
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        test = {}
        for i in s:
            test[i]= test.get(i,0)+1
        for i in t:
            if i not in test:
                return False
            else:
                test[i] -= 1
        for values in test.values():
            if values > 0:
                return False 
        return True

        