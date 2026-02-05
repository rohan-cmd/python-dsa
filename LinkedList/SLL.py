class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.length = 0
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
        self.length = self.length+1

    def deleteLast(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while((temp.next).next):
                    temp = temp.next
                temp.next = None
            self.length = self.length-1

    def insertFirst(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
        self.length = self.length+1

    def deleteFirst(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                self.head = temp.next
                temp.next = None
            self.length = self.length-1

    def getNode(self, ind):
        if ind<0:
            return None
        temp = self.head
        i = 0
        while(temp and i<ind):
            temp = temp.next
            i = i+1
        
        if (temp):
            return temp
        else:
            return None
        
    def setNode(self, ind, val):
        temp = self.getNode(ind)
        if temp:
            temp.data = val

    def insertAtIndex(self, ind, data):
        if ind < 0 or ind > self.length:
            print("Index out of bounds")
            return

        if ind==0:
            self.insertFirst(data)
            return
        
        if ind==self.length:
            self.insertLast(data)
            return
        
        temp = self.getNode(ind-1)
        if (temp):
            newNode = Node(data)
            newNode.next = temp.next
            temp.next = newNode
            self.length = self.length+1
            return
        else:
            return None

    def deleteFromIndex(self, ind):
        if ind < 0 or ind >= self.length:
            print("Index out of bounds")
            return

        if ind==0:
            self.deleteFirst()
            return
        
        if ind==self.length-1:
            self.deleteLast()
            return

        temp = self.getNode(ind-1)
        if temp:
            tempRem = temp.next
            temp.next = tempRem.next
            tempRem.next = None
            self.length = self.length-1

    def reverseLinkedList(self):
        if not (self.length <=1) :
            prev = None
            curr = self.head

            while(curr):
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            
            self.head = prev


    def printLL(self):
        temp = self.head
        while(temp):
            print(temp.data , end=" -> ")
            temp = temp.next
        print("None")
    
    def printLength(self):
        return self.length
    
    def printHead(self):
        if self.head:
            return self.head.data
            
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

    # linkedList.setNode(10, 100)
    linkedList.insertAtIndex(5,100)

    linkedList.printLL()

    linkedList.reverseLinkedList()

    linkedList.printLL()
    print(linkedList.printLength())
    print(linkedList.printHead())