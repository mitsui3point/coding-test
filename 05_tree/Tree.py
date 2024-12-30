class Tree:
    def __init__(self):
        self.root = None
        
class Node:
    def __init__(self, value = None, right = None, left = None):
        self.value = value
        self.left = left
        self.right = right
        
    def __str__(self):
        return f"\nNode(value={self.value}, left={self.left}, right={self.right})"