#node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#linkedlistclass
class LinkedList:
    def __init__(self):
        self.head=None
    #function for inserting node at last of linkedlist
    def insert(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode=lastnode.next
            lastnode.next=newnode
    #printing linkedlist elements
    def printllist(self):
        currentnode=self.head
        if currentnode is None:
            print("linkkedlist is empty")
            return
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode=currentnode.next
    #function for deleting a node which contains given node
    def delete(self,key):
        temp=self.head
        #if node to be deleted is headnode
        if temp is not None:
            if temp.data is key:
                self.head=temp.next
                temp=None
                return
        #if node to be deleted is not headnode
        while (temp is not None):
            if temp.data==key:
                break
            previous=temp
            temp=temp.next
        #if given key is not present in linkedlist
        if temp is None:
            print('given key is not present in linkedlist')
            return
        previous.next=temp.next
        temp=None
        

if __name__=='__main__':
    llist=LinkedList()
    firstnode=Node(1)
    secondnode=Node(2)
    thirdnode=Node(3)
    fourthnode=Node(4)
    llist.insert(firstnode)
    llist.insert(secondnode)
    llist.insert(thirdnode)
    llist.insert(fourthnode)
    print("linkedlist before deleting")
    llist.printllist()
    llist.delete(2)
    print("linkedlist after deleting")
    llist.printllist()
    



    

                