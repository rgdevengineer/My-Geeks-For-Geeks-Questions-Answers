
'''
Slicing in String - Python

Here we'll talk about the novel and perhaps tantalizing concept of slicing. Slicing is the process through which you can extract some continuous part of a string. For example: string is "python", let's use slicing in this. Slicing can be done as:

a. string[0:2] = py (Slicing till index 1)
b. string[0:] = python (Slicing till last index)
c. string[0:4] = pyth (Slicing till index 3)
d. string[0:-2] = pyth (Slicing till index -3).
Note: -1 indexing starts from last of any string.

Now, lets look into this through a question. Given a string of braces named bound_by, and a string named tag_name. The task is to print a new string such that tag_name is in the middle of bound_by.

Example 1:

Input: 
bound_by = [[]], tag_name = tag
Output:
[[tag]]
Example 2:

Input: 
bound_by = <>, tag_name = body
Output:
<body>
Your Task:
Your task is to complete the function join_middle() which should return the modified string.

Constraints:
1 <= |tag_name| <= 103
'''

def join_middle(bound_by, tag_name):
  mid = len(bound_by) // 2
  return bound_by[0:mid] + tag_name + bound_by[mid:]