class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        sqrt = 0
        left = 1
        right = x // 2
        while left <= right:
            mid = (left+right)//2
            mid_sqrt = mid * mid
            if mid_sqrt == x:
                return mid
            elif mid_sqrt < x:
                sqrt = mid 
                left = mid + 1
            else:
                right = mid - 1
        return sqrt