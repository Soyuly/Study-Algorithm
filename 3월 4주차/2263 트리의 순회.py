class Node:
    def __self__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

import sys

n = int(sys.stdin.readline().rstrip())
tree = {}

data = list(map(int,sys.stdin.readline().split()))
    
for i in range(len(data)):
    left_node, data, right_node = i, i+1, i+2

    data[i+1] = Node(i+1, i, i+2)   

