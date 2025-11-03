class Solution:
    def calPoints(self, operations: List[str]) -> int:
        test = []
        for i in range(len(operations)):
            if operations[i] == "C":
                test.pop(-1)
            elif operations[i] == "D":
                test.append(test[-1]*2)
            elif operations[i] == "+":
                test.append(test[-1]+test[-2])
            else:
                test.append(int(operations[i]))
        output= 0 
        for i in range(len(test)):
            output += test[i]
        return output