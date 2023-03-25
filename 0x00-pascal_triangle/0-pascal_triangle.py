#!/usr/bin/python3
'''Module to return pascal triangele'''

def pascal_triangle(n):
'''
pascal's triangle
Args:
n (int): The number of rows of the triangele
Returns:
List of lists of integers representing the pascal`s triangle
'''
lists = []
if n == 0:
return lists
for i in range(n):
lists.append([])
lists[i].append(1)
if (i > 0):
for j in range(1, i):
lists[i].append(lists[i - 1][j - 1] + lists[i -1][j])
lists[i].append(1)
return lists