"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

class LongestCommonPrefix(object):
    def Solution(self, strs):
        if len(strs) == 0:
            return ""
        else:
            a1, a2 = max(strs), min(strs)
            i, match = 0, 0
            while i < len(a1) and i < len(a2) and a1[i] == a2[i]:
                i, match = i+1, match + 1
            return a1[0:match]

output =  LongestCommonPrefix().Solution(["flower","flow","flight"])
print('Output_________',output)

output1 =  LongestCommonPrefix().Solution(["dog","racecar","car"])
print('Output_________',output1)