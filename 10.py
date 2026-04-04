class Solution: #Max Consecutive Ones
    def findMaxConsecutiveOnes(self, nums):
      currentCount = 0
      maxCount = 0
      for num in nums:
        if num == 1:
          currentCount += 1
        else:
          maxCount = max(maxCount, currentCount)
          currentCount = 0
      return max(maxCount, currentCount)
nums = [1,1,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1]
print("Original Array:",nums)
print("Maximum number of consecutive 1's:",Solution().findMaxConsecutiveOnes(nums))

class Solution: #Missing Number
      def missingNumber(self, nums):
          nums.sort()
  
          if nums[0] != 0:
              return 0
  
          for i in range(1, len(nums)):
              if nums[i] != nums[i - 1] + 1:
                  return nums[i - 1] + 1
  
          return len(nums)
nums = [6,0,4,3,1,5]
print("Original Array:",nums)
print("Missing Number:",Solution().missingNumber(nums))
