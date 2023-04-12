nums = [2,3,1,1,4]
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if nums == [0]: return True
        maxDist = 0
        end_index = len(nums)-1
        for i, jump in enumerate(nums):
            if maxDist >= i and i+jump > maxDist:
                maxDist = i+jump
                if maxDist >= end_index:
                    return True
        return False
        
print(Solution().canJump(nums))

    # def canJump(self, nums: list[int]) -> bool:
    #     if len(nums) == 1:
    #         return True
    #     else:
    #         dp = [False] * len(nums)
    #         dp[0] = True
    #         for i in range(1, len(nums)):
    #             block = 0
    #             for j in range(block,i):
    #                 if dp[j] and j + nums[j] >= i:
    #                     dp[i] = True
    #                     block = j
    #                     break
    #         return dp[-1]