class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0 
        max_sum = float('-inf')
        i=0
        while i < len(nums):
            cur_sum += nums[i]
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum <= 0:
                cur_sum = 0 
            i += 1
        return max_sum