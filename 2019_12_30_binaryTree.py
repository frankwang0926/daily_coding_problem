'''
This problem was asked by Google.

Given the root to a binary tree, 
implement serialize(root), which serializes the tree into a string, 
and deserialize(s), which deserializes the string back into the tree.
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(N) time and space

def serialize(root):
    if root == None:
        return "Null"
    return "{} {} {}".format(root.val, serialize(root.left), serialize(root.right))

def helper(list):
    if list[0] == "Null":
        list.pop(0)
        return None
    node = Node(list[0])
    list.pop(0)
    node.left = helper(list)
    node.right = helper(list)
    return node

def deserialize(s):
    list = s.split()
    return helper(list)

'''
def serialize(root):
    if root is None:
        return '#'
    return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))

def deserialize(data):
    def helper():
        val = next(vals)
        if val == '#':
            return None
        node = Node(val)
        node.left = helper()
        node.right = helper()
        return node
    vals = iter(data.split())
    return helper()
'''

node = Node('root', Node('left', Node('left.left')), Node('right'))

print(serialize(node))
print(serialize(deserialize(serialize(node))))
print(deserialize(serialize(node)).left.left.val == 'left.left')