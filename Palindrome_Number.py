"""
Given an integer x, return true if x is a palindrome and false otherwis.

Example 2:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

"""


class Palindrome_Number():
    def isPalindrome(self, input_value):
        total = 0
        a = input_value
        while(input_value > 0):
            b = input_value % 10
            total = total * 10 + b
            input_value = input_value // 10  
        if total == a:
            return True
        else:
            return False

output =  Palindrome_Number().isPalindrome(121)
print('Output_________',output)

output1 =  Palindrome_Number().isPalindrome(123)
print('Output1_________',output1)

