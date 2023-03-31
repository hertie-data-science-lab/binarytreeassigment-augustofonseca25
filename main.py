# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:18:23 2023

@author: Hannah
"""

from mlbt import MutableLinkedBinaryTree
from linkedbinarytree import LinkedBinaryTree


lbt = LinkedBinaryTree()

#print(len(lbt))
#print(lbt.root())

lbt._add_root(1)
lbt._add_left(lbt.root(), 2)
lbt._add_right(lbt.root(), 3)

l = lbt.left(lbt.root())
r = lbt.right(lbt.root())

lbt._add_left(l, 4)
lbt._add_right(l, 5)
lbt._add_left(r, 6)
lbt._add_right(r, 7)



#print(len(lbt))
#print(lbt.height(lbt.root()))

'''
If you want to get the elements of the tree, you need to traverse it.
In this script, you can choose three kind of ordenation: preorder, inorder or postorder.
Where:
- preorder: gets the elements of the node at position p, its left child and its right child.
- inorder: gets the elements of the left child of the node at position p, the node at position p and its right child.
- postorder: gets the elements of the left child of the node at position p, its right child and the node at position p.
'''
# For the preorder from the root, please run the code below.
# If you want to start from another position, just replace the argument "lbt.root()" for the position of the respective node.
print(lbt.preorder_print(lbt.root(),""))

# For the inorder from the root, please run the code below.
# If you want to start from another position, just replace the argument "lbt.root()" for the position of the respective node.
print(lbt.inorder_print(lbt.root(),""))

# For the postorder from the root, please run the code below.
# If you want to start from another position, just replace the argument "lbt.root()" for the position of the respective node.
print(lbt.postorder_print(lbt.root(),""))

