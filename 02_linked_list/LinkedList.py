from Node import Node

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def insert_back(self, value):
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
        
    # TODO: insert_at 구현
    def insert_at(self, idx, value):
        new_node = Node(value)
        current = self.head
        if self.head == None:
            self.head = new_node
            return
        if idx == 0:
            new_node.next = current
            self.head = new_node
            return
        for _ in range(0, idx - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def __str__(self):
        return f"LinkedList(header={self.head})"