nums = [1,2,1,1]

class Solution:
    def rob1(self, nums: list[int]) -> int:
        f0 = f1 = 0
        for i, x in enumerate(nums):
            f0, f1 = f1, max(f1, f0 + x)
        return f1

    def rob(self, nums: list[int]) -> int:
        return max(nums[0] + self.rob1(nums[2:-1]), self.rob1(nums[1:]))

        

print(Solution().rob(nums))