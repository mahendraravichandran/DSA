class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # what I think is first we can create a list and add each element to a list and when the hashtag is present we can just pop the last element 
        stackA = []
        stackB = []
        for i in range(len(s)):
            if s[i]=="#":
                if stackA:
                    stackA.pop()
            else:
                stackA.append(s[i]) 
        for i in t:
            if i == "#":
                if stackB:
                    stackB.pop()
            else:
                stackB.append(i)
        
        return stackA == stackB
            

