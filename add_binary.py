"""
Companies
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""

def add_binary(x, y):
    max_len = max(len(x), len(y))

    x = x.zfill(max_len)
    y = y.zfill(max_len)
    result = ''
    output = 0
    
    for i in range(max_len - 1, -1, -1):
        r = output
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        output = 0 if r < 2 else 1   
         
    if output !=0 : result = '1' + result
    return result.zfill(max_len)

print("result1--------",add_binary('11', '1'))
print("result2--------",add_binary('1010', '1011'))
