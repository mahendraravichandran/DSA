class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        if target > nums[right]:
            return right+1
        while left <= right:
            m = (left+right)//2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                right = m - 1
            else:
                left = m + 1
        return left
           
            
            