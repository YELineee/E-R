nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]

class Solution:
    def jump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return 0
        else:
            dp = [0] * len(nums)
            dp[0] = 0
            for i in range(1, len(nums)):
                block = 0
                for j in range(block,i):
                    if dp[j] != 0 and j + nums[j] >= i:
                        dp[i] = dp[j] + 1
                        block = j
                        break
            return dp[-1]

print(Solution().jump(nums))