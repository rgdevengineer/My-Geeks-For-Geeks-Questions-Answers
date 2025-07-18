
'''
Set in Python - II

This is the last practice question of Python Set. You are familiar with working on the set in Python. Now, let's move on to work on two sets using some inbuilt functions which are used widely. They are:
union(): Used to find union() between two sets. It performs this using '|' operator.
intersection(): Used to find intersection() between two sets. It performs this using '&' operator.
difference(): Difference of A and B (A - B) is a set of elements that are only in A but not in B. Similarly for B - A holds the same.

Now, Given some elements in two sets a and b, the task is to find the elements common in two sets, elements in both the sets, elements that are only in set a, not in b.

Example:

Input:
a = {1, 2, 3, 4, 5}
b = {6, 7, 8, 2, 3}
Output:
1 2 3 4 5 6 7 8
2 3
1 4 5
Your Task:
Your task is to complete the function all_in_set(), common_in_set() and diff() to perform union, intersection and difference between two sets and return the elements in the set after each operation.

Constraints:
1 <= S[i] <= 104
'''

def common_in_set(a, b):
    return a.intersection(b)
    
def diff(a, b):
    return a.difference(b)

def all_in_set(a, b):
    return a.union(b)
    
    
    