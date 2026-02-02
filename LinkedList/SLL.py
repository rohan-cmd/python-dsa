class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
    
    def insertLast(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else : 
            newNode = Node(data)
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = newNode
        self.size = self.size+1

    def deleteLast(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while((temp.next).next):
                    temp = temp.next
                temp.next = None
            self.size = self.size-1

    def insertFirst(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
        self.size = self.size+1

    def deleteFirst(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                self.head = temp.next
                temp.next = None
            self.size = self.size-1

    def printLL(self):
        temp = self.head
        while(temp):
            print(temp.data , end=" -> ")
            temp = temp.next
        print("None")
    
    def printSize(self):
        return self.size
            
if __name__ == "__main__" :
    linkedList = SinglyLinkedList()

    # linkedList.insertLast(2)
    # linkedList.insertLast(4)
    # linkedList.insertLast(6)

    linkedList.insertFirst(2)
    linkedList.insertFirst(4)
    linkedList.insertFirst(6)
    linkedList.insertFirst(8)
    linkedList.insertFirst(10)

    linkedList.printLL()
    print(linkedList.printSize())