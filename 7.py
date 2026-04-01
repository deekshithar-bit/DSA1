class Solution(object):
  def isPowerOfTwo(self, n):
    """
    :type n: int
    :rtype: bool
    """
    if n == 1:
      return True
    elif n < 1 or n % 2 != 0:
      return False
    return self.isPowerOfTwo(n // 2)
n = 16
result = Solution().isPowerOfTwo(n)
print("Is Power of Two:",result)
