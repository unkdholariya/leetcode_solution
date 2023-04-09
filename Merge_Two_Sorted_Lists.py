"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""
list1 =[1,2,4]
list2 = [1,3,4]

result_list1 = sorted(list1 + list2)

print ("The combined sorted list is : " + str(result_list1))

list3 = []
list4 = []

result_list2 = sorted(list3 + list4)

print ("The combined sorted list is : " + str(result_list2))

list5 = []
list6 = [0]

result_list3 = sorted(list5 + list6)

print ("The combined sorted list is : " + str(result_list3))

