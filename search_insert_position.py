"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

"""

def find_index(nums, a, b):
    for i in range(a):
        if nums[i] == b:
            return i
        elif nums[i] > b:
            return i
    return a

nums = [1, 3, 5, 6]
a = len(nums)
b = 5
print("output1__________________",find_index(nums, a, b))

nums = [1, 3, 5, 6]
a = len(nums)
b = 2
print("output2__________________",find_index(nums, a, b))