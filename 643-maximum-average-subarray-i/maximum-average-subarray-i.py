class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        win_sum = 0
        while i < k:
            win_sum = win_sum + nums[i]
            i +=1
        bes_sum = win_sum
        left = 0
        right = k
        while right < len(nums):
            win_sum = win_sum + nums[right] - nums[left]
            left +=1
            right +=1
            if win_sum > bes_sum:
                bes_sum = win_sum
        return bes_sum/k
            


