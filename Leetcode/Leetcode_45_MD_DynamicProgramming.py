nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]

class Solution:
    def jump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return 0
        else:
            max = len(nums) - 1
            min = 1
            while max >= min:
                
print(Solution().jump(nums))