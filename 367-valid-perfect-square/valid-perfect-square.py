class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True 
        l, r  = 1, num // 2
        while l <= r:
            mid =(l + r) // 2
            mid_sqr = mid * mid
            if mid_sqr == num:
                return True
            elif mid_sqr < num:
                l = mid + 1
            else:
                r = mid - 1
        return False