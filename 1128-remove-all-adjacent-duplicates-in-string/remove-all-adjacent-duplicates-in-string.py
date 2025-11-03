class Solution:
    def removeDuplicates(self, s: str) -> str:
        t=[]
        for i in s:
            if t and i == t[-1]:
                t.pop()
            else:
                t.append(i)
        result =""
        for i in t:
            result=result+i
        return result