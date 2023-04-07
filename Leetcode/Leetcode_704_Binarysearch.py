nums = [-1,0,3,5,9,12]
target = 9
# 二分查找，找到target的下标，没有返回-1

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

s = Solution()
print(s.search(nums, target))