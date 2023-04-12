num = 1
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left < right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid
            elif mid * mid <= num:
                left = mid + 1
            elif right == 1:
                return True
        return False
    
print(Solution().isPerfectSquare(num))