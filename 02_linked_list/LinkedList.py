from Node import Node

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return

        current = self.head
        while (current.next):
            current = current.next
        current.next = new_node

    def get(self, idx):
        index = 0
        current = self.head
        while (index != idx):
            current = current.next
            index += 1
        return current

    def __str__(self):
        return f"LinkedList(header={self.head})"