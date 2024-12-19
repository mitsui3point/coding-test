from Node import Node

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node

        current = self.head
        while (current):
            current = current.next
        current = new_node

    def __str__(self):
        return f"LinkedList(header={self.head})"