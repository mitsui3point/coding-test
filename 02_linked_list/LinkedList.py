from Node import Node

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node

        current = self.head
        while (current.next):
            current = current.next
        current.next = new_node

    def __str__(self):
        return f"LinkedList(header={self.head})"