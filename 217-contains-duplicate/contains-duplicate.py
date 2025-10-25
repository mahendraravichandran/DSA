class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        test = {}
        for i in nums:
            if i in test:
                return True
            else:
                test[i] = 1
        return False
