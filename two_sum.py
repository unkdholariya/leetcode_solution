"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

class two_sum():  
    def __init__(self, num_list, target):  
        self.num_list = num_list  
        self.target = target  
          
    def solution(self):  
        length = len(num_list)  
        for i in range(length-1):  
            for j in range(i+1, length):  
                if num_list[i]+num_list[j] == self.target:   
                    return [i,j]  
                
num_list = [2,7,11,15]  
target = 9  
obj = two_sum(num_list, target)  
print("Output__________",obj.solution())  