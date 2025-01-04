class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return f"Node(value={self.value})"