nums = [1,2,1,1]

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums) - 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            if nums[0] > nums[1]:
                dp[-1] = dp[-2]
            else:
                dp[-1] = max(dp[-2] + nums[0], nums[-1]+dp[-3]-nums[0],dp[-3])
            return dp[-1]
        

print(Solution().rob(nums))