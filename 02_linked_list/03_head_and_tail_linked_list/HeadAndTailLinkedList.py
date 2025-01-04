from Node import Node  # Node.py에서 Node 클래스를 가져옴

# insert_back(O(1))
class HeadAndTailLinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    
    def insert_back(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            return
        self.tail.next = new_node
        self.tail = self.tail.next

    def get(self, idx):
        if self.head == None:
            raise Exception('empty linkedList')
        current = self.head
        for _ in range(0, idx):
            current = current.next
        return current
    
    def insert_at(self, idx, value):
        new_node = Node(value)
        # 비어있을 경우
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            return
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(0, idx - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, idx):
        if self.head == None:
            return
        if idx == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(0, idx - 1):
            current = current.next
        current.next = current.next.next