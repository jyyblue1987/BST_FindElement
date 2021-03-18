
from __future__ import annotations  # allow self-reference
from typing import List, Optional


class TreeNode:
    """Tree Node that contains a value as well as left and right pointers"""
    def __init__(self, val: int, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)

    return root
def findGreatest(root, key):    
    val = None
    while root:
        val1 = root.val
        if val1 < key:
            val = val1
            root = root.right
        else:
            root = root.left

    if val == None:
        return None

    if val > key:
        return None

    return val


def rewind_combo(points: List[int]) -> List[Optional[int]]:
    root = None
    r = None
    index = 0
    result = []
    for p in points:
        q = findGreatest(root, p)
        result.append(q)
        if r is None:
            r = TreeNode(p)
            root = r
        else:
            r = insert(r, p)

        index = index + 1

    return result


# class Node: #Class node for tree
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key


# def insert(root, key): #Function for inserting new node to tree
#     if root is None: #If there is not any node in tree, then return it to root
#         return Node(key)
#     else:
#         if root.val == key: #For remove duplicate
#             return root
#         elif root.val < key: #If key is greate than root
#             root.right = insert(root.right, key)
#         else: #If key is less than root
#             root.left = insert(root.left, key)
#     return root

# def largest_ancestor(root, n, largest): #For largest element which is smaller than n, return None if not found
#     if root is None:
#         return None
#     if(root.val < n): #If n is greater than root then search on the right side
#         return largest_ancestor(root.right, n, root.val)
#     elif(root.val > n): #If root is greater than n then serach on the left side
#         return largest_ancestor(root.left, n, largest)
#     elif(root.val == n): #Once it is eqaul to n, then return largest
#         return largest
  

# def rewind_combo(points): #Function for getting the modified version of given array
#     i = 0
#     root = Node(points[i]) #Insert first element of list in root
#     for i in range(1,len(points)): #Insert all the elements in bst
#         root = insert(root,points[i])

#     rewind = [] #Empty list to store the rewind version of original list
#     for i in points:
#         rewind.append(largest_ancestor(root, i, None)) #Store the value in rewind list

#     return rewind #Return list
