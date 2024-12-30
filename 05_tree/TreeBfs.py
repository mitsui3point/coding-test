
from collections import deque
from Tree import Tree, Node


def bfs(root = None):
    if root == None:
        return None
    visited = []
    q = deque()
    q.append(tree.root)
    while q:
        current = q.popleft()
        visited.append(current.value)
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
    return visited

if __name__ == '__main__':
    tree = Tree()
    tree.root = Node(value = 'A')
    tree.root.left = Node(value = 'B')
    tree.root.right = Node(value = 'C')
    tree.root.left.left = Node(value = 'D')
    tree.root.left.right = Node(value = 'E')
    tree.root.right.right = Node(value = 'F')
    tree.root.left.left.left = Node(value = 'G')
    tree.root.left.left.right = Node(value = 'H')
    print(bfs(tree.root))            