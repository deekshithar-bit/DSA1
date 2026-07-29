class Solution: # Jump Game DP
    def canJump(self, nums):
        end = len(nums) - 1
        dp = [-1] * len(nums)

        def dfs(start):
            if start == end:
                return True

            if dp[start] != -1:
                return dp[start]

            ans = False

            for i in range(1, nums[start] + 1):
                if not ans and start + i <= end:
                    ans = ans or dfs(start + i)

            dp[start] = ans
            return ans

        return dfs(0)


# Driver code
nums = [2, 3, 1, 1, 4]

obj = Solution()
print(obj.canJump(nums))