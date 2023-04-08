nums = [-4,-1,0,3,10]

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([i ** 2 for i in nums])
    
print(Solution().sortedSquares(nums))
