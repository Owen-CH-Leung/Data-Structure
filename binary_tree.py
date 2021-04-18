class binary_tree:
    def __init__(self, data = None):
        self.data = data 
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = binary_tree(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = binary_tree(data)
        else:
            self.data = data
                    
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()
    
    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)
    
    def search(self, data):
        if data < self.data:
            if not self.left:
                return f"Cannot find {data}"
            return self.left.search(data)
        elif data > self.data:
            if not self.right:
                return f"Cannot find {data}"
            return self.right.search(data)
        else:
            return f"Found {data}"
            
if __name__ == '__main__':
    b_tree = binary_tree()
    data = [10, 12, 5, 26, 17, 39, 33]
    for d in data:
        b_tree.insert(d)
    print('inorder :')
    b_tree.inorder()
    print('preorder :')
    b_tree.preorder()
    print('postorder :')
    b_tree.postorder()
    print('search :')
    b_tree.search(5)
    b_tree.search(1000)