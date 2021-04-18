class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
        
class doubly_linked_list:
    def __init__(self):
        self.head = None

    # for inserting at beginning of linked list
    def insertAtStart(self, data):
        if self.head == None:
            newnode = node(data)
            self.head = newnode
        else:
            newnode = node(data)
            self.head.previous = newnode
            newnode.next = self.head
            self.head = newnode

    # for inserting at end of linked list
    def insertAtEnd(self, data):
        newnode = node(data)
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newnode
        newnode.previous = temp

    # deleting a node from linked list
    def delete(self, data):
        temp = self.head
        if(temp.next != None):
            # if head node is to be deleted
            if(temp.data == data):
                temp.next.previous = None
                self.head = temp.next
                temp.next = None
                return
            else:
                while(temp.next != None):
                    if(temp.data == data):
                        break
                    temp = temp.next
                if(temp.next):
                    # if element to be deleted is in between
                    temp.previous.next = temp.next
                    temp.next.previous = temp.previous
                    temp.next = None
                    temp.previous = None
                else:
                    # if element to be deleted is the last element
                    temp.previous.next = None
                    temp.previous = None
                return

        if (temp == None):
            return

    def print_all(self):
        temp = self.head
        while(temp != None):
            print(temp.data, end=' ')
            temp = temp.next
            
if __name__ == '__main__':
    doubly_linked_list = doubly_linked_list()
    doubly_linked_list.insertAtStart(1.5)
    doubly_linked_list.insertAtStart(2.4)
    doubly_linked_list.insertAtEnd(30)
    doubly_linked_list.insertAtStart(4.3)
    doubly_linked_list.print_all()
    
    
    