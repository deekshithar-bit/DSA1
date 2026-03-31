class Solution(object): #Removing Duplicates from Sorted Array
      def removeDuplicates(self, nums):
          x = 0
          for i in range(len(nums)):
              if nums[i] > nums[x]:
                  x += 1
                  nums[x] = nums[i]
          return x + 1
nums = [1,2,6,2,5,3] 
result = Solution().removeDuplicates(nums)
print("Length of array after removing duplicates:",result)  

class Solution(object): #Removing Element 
  def removeElement(self, nums, val):
    x = 0
    for i in range(len(nums)):
      if nums[i] != val:
        nums[x] = nums[i]
        x += 1
    return x
nums = [1,2,3,6,5,8,3,9,2,6,0]
val = 3
result = Solution().removeElement(nums,val)  
print("Length of the array after removing elements:",result)
