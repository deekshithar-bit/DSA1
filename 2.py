class Solution(object):
    def reverse(self, x):
        rev = 0
        n = abs(x)
        while n != 0:
            last = n % 10
            rev = rev * 10 + last
            n //= 10
        if rev > 2**31 - 1:
            return 0
        return -rev if x < 0 else rev

sol = Solution()
print(sol.reverse(763342))