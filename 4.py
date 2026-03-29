class Solution(object): #Binary Search 
    def search(self, nums, target):
      """
      :type nums: List[int]
      :type target: int
      :rtype: int
      """
      left = 0
      right = len(nums) - 1
  
      while left <= right:
        middle = (left + right) // 2
  
        if nums[middle] == target:
          return middle
        elif target < nums[middle]:
          right = middle - 1
        else:
          left = middle + 1
  
      return -1
nums = [1, 2, 3, 4, 5]
target = 3

result = Solution().search(nums, target)
print("Index:", result)      