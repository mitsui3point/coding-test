from Tree import Tree, Node

def dfs(root):
    """
    탐색
    """
    if root is None:
        return
    dfs(root.left)
    dfs(root.right)

def pre_order(current_root):
    """
    전위순회: 처음 방문
    """
    if current_root is None:
        return
    print('pre  ', current_root.value)
    pre_order(current_root.left)
    pre_order(current_root.right)
    
def in_order(current_root):
    """
    중위순회: 중간에 방문
    """
    if current_root is None:
        return
    in_order(current_root.left)
    print('in   ', current_root.value)
    in_order(current_root.right)
    
def post_order(current_root):
    """
    후위순회: 마지막에 방문
    """
    if current_root is None:
        return
    post_order(current_root.left)
    post_order(current_root.right)
    print('post ', current_root.value)
    


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
    pre_order(tree.root)
    print('='*30)
    in_order(tree.root)
    print('='*30)
    post_order(tree.root)