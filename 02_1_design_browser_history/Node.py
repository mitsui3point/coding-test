class Node:
    def __init__(self, value = None, next = None, prev = None):
        if value is None:
            raise Exception('value is not allowed empty')
        self.value = value
        self.next = next
        self.prev = prev
        
    def __str__(self):
        return f"Node(value={self.value}, prev={self.prev}, next={self.next})"