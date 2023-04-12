arr = [0,1,2,3,4,5,3,2,1]
class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left