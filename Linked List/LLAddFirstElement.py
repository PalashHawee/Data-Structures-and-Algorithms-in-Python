class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addlast(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def display(self):
        p = self._head
        while p:
            print(p._element,end='-->')
            p = p._next
        print()

    def search(self,key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._next
            index = index + 1
        return -1
    #Adding in the beginning of the list 
    #Time complexity is O(1)   
    def addfirst(self, t):
        newest = _Node(t, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size += 1

L = LinkedList()
L.addlast(7)
L.addlast(4)
L.addlast(12)
L.addlast(8)
L.addlast(3)
L.display()
print('Size:',len(L))
L.addfirst(15)
L.display()
print('Size:',len(L))
L.addfirst(25)
L.display()
print('Size:',len(L))
L.addlast(35)
L.display()
print('Size:',len(L))
