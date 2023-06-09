numbers = [2,7,11,15]
target = 9
def twoSum(self, numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1
    while 1:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1
