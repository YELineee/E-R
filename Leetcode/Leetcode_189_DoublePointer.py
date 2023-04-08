nums = [-1,-100,3,99]
k = 2

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(num)
        nums[:] = nums[-k:] + nums[:-k]

print(Solution().rotate(nums, k))