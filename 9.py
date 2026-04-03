class Solution(object): #Merge Sorted Arrays
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()
nums1 = [1,2,3,4,5,0,0,0]
m = 5
nums2 = [2,5,6]
n = 3
print("Original Array:", nums1)
Solution().merge(nums1, m, nums2, n)
print("Merged Array:", nums1)      

class Solution: #Move Zeroes
    def moveZeroes(self, nums):
      x = 0
      for i in range(len(nums)):
        if nums[i] != 0:
          nums[x] = nums[i]
          x += 1
      for i in range(x, len(nums)):
        nums[i] = 0
nums=[0,1,0,3,12,4,0,5]        
Solution().moveZeroes(nums)
print("Array after moving zeros:", nums)
