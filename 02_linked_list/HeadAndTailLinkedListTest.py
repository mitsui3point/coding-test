from HeadAndTailLinkedList import HeadAndTailLinkedList  # Node.py에서 Node 클래스를 가져옴

# insert_back(O(1))
if __name__ == "__main__":
    headAndTailLinkedList = HeadAndTailLinkedList()
    headAndTailLinkedList.insert_back(4)
    headAndTailLinkedList.insert_back(3)
    headAndTailLinkedList.insert_back(2)
    headAndTailLinkedList.insert_back(1)
    print('headAndTailLinkedList.get(0)', headAndTailLinkedList.get(0))
    print('headAndTailLinkedList.get(1)', headAndTailLinkedList.get(1))
    print('headAndTailLinkedList.get(2)', headAndTailLinkedList.get(2))
    print('headAndTailLinkedList.get(3)', headAndTailLinkedList.get(3))
    headAndTailLinkedList.insert_at(0, 100)
    print('=======================================')
    print('headAndTailLinkedList.get(0)', headAndTailLinkedList.get(0))
    print('headAndTailLinkedList.get(1)', headAndTailLinkedList.get(1))
    print('headAndTailLinkedList.get(2)', headAndTailLinkedList.get(2))
    print('headAndTailLinkedList.get(3)', headAndTailLinkedList.get(3))
    print('headAndTailLinkedList.get(4)', headAndTailLinkedList.get(4))
    headAndTailLinkedList.delete(4)
    print('=======================================')
    print('headAndTailLinkedList.get(0)', headAndTailLinkedList.get(0))
    print('headAndTailLinkedList.get(1)', headAndTailLinkedList.get(1))
    print('headAndTailLinkedList.get(2)', headAndTailLinkedList.get(2))
    print('headAndTailLinkedList.get(3)', headAndTailLinkedList.get(3))