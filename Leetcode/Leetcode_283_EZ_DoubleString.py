nums = [0,0,1,0,0,1]

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        for i in range(len(nums) + x):
            if nums[i - x] == 0:                
                nums.append(nums.pop(i - x))   
        return nums

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         n, left, right = len(nums), 0, 0
#         while right < n:
#             if nums[right] != 0:
#                 nums[right], nums[left] = nums[left], nums[right]
#                 left += 1
#             right += 1 