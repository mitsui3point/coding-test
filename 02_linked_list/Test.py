from Node import Node  # Node.py에서 Node 클래스를 가져옴
from LinkedList import LinkedList  # Node.py에서 Node 클래스를 가져옴

if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.insert_back(4)
    linkedList.insert_back(3)
    linkedList.insert_back(2)
    linkedList.insert_back(1)
    print('linkedList.get(0)', linkedList.get(0))
    print('linkedList.get(1)', linkedList.get(1))
    print('linkedList.get(2)', linkedList.get(2))
    print('linkedList.get(3)', linkedList.get(3))
    linkedList.insert_at(0, 100)
    print('=======================================')
    print('linkedList.get(0)', linkedList.get(0))
    print('linkedList.get(1)', linkedList.get(1))
    print('linkedList.get(2)', linkedList.get(2))
    print('linkedList.get(3)', linkedList.get(3))
    print('linkedList.get(4)', linkedList.get(4))

