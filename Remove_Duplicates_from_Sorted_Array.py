"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

class RemoveDublicateSolution():
    def Solution(self, nums):
        if not nums:
            return 0     
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
        return (i + 1)
    
nums = [1,2,2,3,3,4,5]
a = RemoveDublicateSolution()
output = a.Solution(nums)
print("Output_________",output)

class RemoveDublicate(object):
   def Solution(self, nums):
      if len(nums) == 0:
         return 0
      length = 1
      previous = nums[0]
      index = 1
      for i in range(1,len(nums)):
         if nums[i] != previous:
            length += 1
            previous = nums[i]
            nums[index] = nums[i]
            index+=1
      return length
nums = [1,1,2,2,2,3,3,3,3,4,5,5,5,6]
b = RemoveDublicate()
output2= b.Solution(nums)
print("Output2_________",output2)
