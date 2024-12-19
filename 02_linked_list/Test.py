from Node import Node  # Node.py에서 Node 클래스를 가져옴
from LinkedList import LinkedList  # Node.py에서 Node 클래스를 가져옴

if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.append(1)
    print('linkedList.header', linkedList.head)
    linkedList.append(2)
    print('linkedList.header.next', linkedList.head.next)
    linkedList.append(3)
    print('linkedList.header.next.next', linkedList.head.next.next)
    # print(first.next)
    # print(first.next.next)
    