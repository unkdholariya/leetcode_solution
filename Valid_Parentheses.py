"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

"""
class ValidParantheses():
   def Solution(self, input_parantheses):
        p_pair =  {"(": ")", "{": "}", "[": "]"}
        O_list = []
        for parenthese in input_parantheses:
            if parenthese in p_pair:
                O_list.append(parenthese)
            elif len(O_list) == 0 or p_pair[O_list.pop()] != parenthese:
                return False
        return len(O_list) == 0
   
output =  ValidParantheses().Solution("(){}[]")
print('Output_________',output)

output2 =  ValidParantheses().Solution("()")
print('Output2_________',output2)

output3 =  ValidParantheses().Solution("()[{)}")
print('Output3_________',output3)

