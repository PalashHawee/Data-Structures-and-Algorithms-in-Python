class Node:
    __slots__ = 'data', 'next'

    def __init__(self, data, next):
        self.data = data
        self.next = next

class StacksLinked:
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def isempty(self):
        return self.size == 0

    def push(self, e):
        newest = Node(e, None)
        if self.isempty():
            self.top = newest
        else:
            newest.next = self.top
            self.top = newest
        self.size += 1

    def pop(self):
        if self.isempty():
            print('Stack is empty')
            return
        e = self.top.data
        self.top = self.top.next
        self.size -= 1
        return e

    def top(self):
        if self.isempty():
            print('Stack is empty')
            return
        return self.top.data

    def display(self):
        p = self.top
        while p:
            print(p.data,end='-->')
            p = p.next
        print()


S = StacksLinked()
S.push(5)
S.push(3)
print(len(S))
S.display()
print(S.pop())
print(S.isempty())

print(S.pop())
print(S.isempty())
S.push(7)
S.push(9)
print(S.top())
S.push(4)
print(len(S))
print(S.pop())
S.push(6)
S.push(8)
print(S.pop())