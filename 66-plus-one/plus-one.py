class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        test = 0
        for i in digits:
            test = test*10 + i
        test += 1
        test = str(test)
        test1 = []
        for i in test:
            test1.append(int(i))
        return test1