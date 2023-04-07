n = 2
bad = 1

class Solution:
    
    
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            if  self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
    
    def isBadVersion(self, n):
        if n >= bad:
            return True
        else:
            return False
    
print(Solution().firstBadVersion(n))

# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         left,right = 0,n
#         while left<right:
#             mid = (left+right)//2
#             if isBadVersion(mid):
#                 #答案在区间[left, mid] 中
#                 right = mid
#             else:
#                 # 答案在区间[mid+1, right] 中
#                left = mid+1
#         return left

