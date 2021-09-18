# Group Project 1
# SCS 341 Algorithms Analysis
# Group Omega
# Lucas Weakland
#NOTE FOR BRAD : I have spent well over 20 something hours this week on this project and got no where
# so this is what I have. It is fully hard coded / brute force. Enjoy. 

# Imports (a lot of testing as we can see)
import random
import sys
from idlelib.tree import TreeNode
from os import name
from random import randint
from binarytree import Node
from binarytree import build
import array as arr

# User input that I never used
# Ask user for how many nodes
#print("How many nodes would you like?")
# take input from user
#input_a = input()
# type cast into integer
#input_a = int(input_a)
# Generate random numbers between 1 and 100 with the amount of the users input
#randomlist = random.sample(range(1, 100), input_a)

# Test array for testing calling numbers for greedy and optimal that i didnt use lol
#a = arr.array('i', (randomlist))

# User input
userInput = int(input("Enter the number of nodes (ps: only put in 6, thx):\n"))
nodes = [0] * userInput
for i in range(userInput):
    nodes[i] = random.randint(1,100)

#Binary tree build
binary_tree = build(nodes)
print('binary tree', binary_tree)
print('list of tree values ', binary_tree.values)

#test for greedy algorithm
if nodes[1] > nodes[2] and nodes[3] > nodes[4]:
        print("Greedy path is: Go down left the whole way")
elif nodes[1] > nodes[2] and nodes[3] < nodes[4]:
        print("Greedy path is: Go down left and take a right")
elif nodes[1] < nodes[2]:
        print("Greedy path is: Go down and take a right til the end")

#test for optimal algorithm
if nodes[1] + nodes[3] > nodes[1] + nodes[4] and nodes[1] + nodes[3] > nodes[2] + nodes[5]:
    print("Optimal path is: down-left, and down-left")
elif nodes[1] + nodes[4] > nodes[1] + nodes[3] and nodes[1] + nodes[4] > nodes[2] + nodes[5]:
    print("Optimal path is: down-left, and down-right")
elif nodes[2] + nodes[5] > nodes[1] + nodes[3] and nodes[2] + nodes[5] > nodes[1] + nodes[4]:
    print("Optimal path is: down right and down")

#testing stuff that didnt end up being used
#if binary_tree.right.values > binary_tree.left.values:
#    print(binary_tree.right.values)
#elif binary_tree.right.values < binary_tree.left.values:
#    print(binary_tree.left.values)

#arr2 = arr.array('i', (binary_tree.right.values))
#print(arr2)

#if arr2[0] + arr2[1] > arr2[0] + arr2[2]:
#    print("The optimal path is to go down:", arr2[0], arr2[1])
#elif arr2[0] + arr2[1] < arr2[0] + arr2[2]:
#    print("The optimal path is to go down:", arr2[0], arr2[2])


