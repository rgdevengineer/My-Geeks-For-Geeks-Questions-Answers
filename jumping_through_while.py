
'''
Jumping through While - Python

Now you are familiar with While loop in Python. Let's get deeper into understanding it through below question.

Given a positive integer x, the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).

Example:

Input:
x = 10
Output:
1 4 9
Explanation:
From 1 to 10, numbers in powers
of 2 are, 12, 22, 32 as 1, 4 and 9.
Your Task:
This is a function problem. You need to complete the function printIncreasingPower().

Constraints:
2 <= x <= 103
'''

def printIncreasingPower(x):
    n = 1
    while n*n <= x:
        print (n*n , end = " ")
        n += 1
        