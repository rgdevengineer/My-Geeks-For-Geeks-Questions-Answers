
'''
Intro to Dictionary - Python

Initialization:

dict = {}
Setting values:

dict['a'] = 1 
dict['b'] = 2
Fetching values:

dict['a'] gives 1 as output 
dict['b'] gives 2 as output
Moving on to the question to implement a dictionary. Given a list of strings containing names of students and another list containing marks of corresponding students. The task is to create a dictionary to store marks of students with their names (name will be unique).

Example:

Input: 
N = 5 
names = [john, ala, ilia, sudan, mercy] 
marks = [100, 200, 150, 80, 300]
Output:
ala 200 
ilia 150 
john 100 
mercy 300 
sudan 80
Your Task:
The task is to complete the function create_dict() which takes arr as input and creates a dictionary then returns it.

Constraints:
1 <= N <= 104
1 <= marks <= 104
'''

def create_dict(arr):

    dict = {}

    for name, marks in arr:
        dict[name] = marks

    return dict