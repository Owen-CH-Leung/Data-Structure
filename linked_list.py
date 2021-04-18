class node:
    def __init__(self, data):
        self.data = data
        self.next_pointer = None
        
class linked_list:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next_pointer
    
    def insert_at_start(self, data):
        if self.head == None:
            self.head = node(data)
        else:
            new_node = node(data)
            new_node.next_pointer = self.head
            self.head = new_node
    
    def insert_at_end(self, data):
        newNode = node(data)
        temp = self.head
        while(temp.next_pointer != None):
            temp = temp.next_pointer
        temp.next_pointer = newNode

    def rm_node(self, data):
        temp = self.head
        if (temp.next_pointer is not None):
            if(temp.data == data):
                self.head = temp.next_pointer
                return
            else:
                #  else search all the nodes
                while(temp.next_pointer != None):
                    if(temp.data == data):
                        break
                    prev = temp
                    temp = temp.next_pointer

                if temp == None:
                    return

                prev.next_pointer = temp.next_pointer
                return

if __name__ == '__main__':
    data1, data2, data3, = 50, 'A string', [6,7,8]
    list_ = linked_list()
    list_.insert_at_start(data1)
    list_.insert_at_end(data2)
    list_.insert_at_start(data3)
    list_.print_list()
    list_.rm_node(data3)
    list_.print_list()