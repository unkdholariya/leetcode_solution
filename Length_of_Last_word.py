"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
"""
class Solution():
    def lengthOfLastWord(a):
        l = 0
        x = a.strip()
        for i in range(len(x)):
            if x[i] == " ":
                l = 0
            else:
                l += 1
        return l
    
print("output1_______",Solution.lengthOfLastWord("Hello World"))
print("output1_______",Solution.lengthOfLastWord("   fly me   to   the moon  "))

