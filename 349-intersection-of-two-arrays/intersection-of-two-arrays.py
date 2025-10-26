class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        test = {}
        output = []
        for i in nums1:
            test[i] = test.get(i,0)+1
        for i in nums2:
            if i in test and i not in output:
                output.append(i)
        return output