class Node:

    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def insert(self, key, value):
        
        if self.key:
            if key < self.key:
                if self.left:
                    self.left.insert(key, value)
                else:
                    self.left = Node(key, value)
            elif key > self.key:
                if self.right:
                    self.right.insert(key, value)
                else:
                    self.right = Node(key, value)
            else:
                raise ValueError('Duplicate values are not allowed: The key already exists!')
        else:
            self.key = key
            self.value = value

    def findValue(self, key):
        if key < self.key:
            if self.left:
                self.left.findNode(key)
            else:
                raise ValueError(f'{key} is not in the tree')
        elif key > self.key:
            if self.right:
                self.right.findNode(key)
            else:
                raise ValueError(f'{key} is not in the tree')
        else:
            return value

    def traverse(self):
        if self.left:
            self.left.traverse()
        print(f'key: {self.key}, value: {self.value}')
        if self.right:
            self.right.traverse()

def test1():
    n1 = Node(11, 'k')
    n1.insert(12, 'a')
    n1.insert(6, 'b')
    n1.insert(14, 'c')
    n1.insert(10, 'd')
    n1.traverse()

test1()
