n = 4
class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return n if n != 2 else 1
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range (2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]
print(Solution().tribonacci(n))
