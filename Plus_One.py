"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
"""

def AddOne(digits):
	index = len(digits) - 1
	while (index >= 0 and digits[index] == 9):
		digits[index] = 0
		index -= 1

	if (index < 0):
		digits.insert(0, 1)
	else:
		digits[index]+=1

digits = [1, 7, 8, 9]
AddOne(digits)
for digit in digits:
	print(digit, end =' ')
	

