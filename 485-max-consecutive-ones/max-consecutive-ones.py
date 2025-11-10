class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left , right = 0, 0
        count = 0
        output = 0
        while right <= len(nums)-1:
            if nums[right] == 1:
                count +=1
                right += 1
            else:
                if count > output:
                    output = count
                    count = 0
                else:
                    count = 0
                left = right +1
                right += 1
            output = max(count,output)
        return output
