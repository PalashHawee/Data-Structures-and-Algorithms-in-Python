# Python Program for Representation of
# Sparse Matrix into Linked List
 
# Node Class to represent Linked List Node
class Node:
 
    # Making the slots for storing row,
    # column, value, and address
    __slots__ = "row", "col", "data", "next"
 
    # Constructor to initialize the values
    def __init__(self, row=0, col=0, data=0, next=None):
 
        self.row = row
        self.col = col
        self.data = data
        self.next = next
 
 
# Class to convert Sparse Matrix
# into Linked List
class Sparse:
 
    # Initialize Class Variables
    def __init__(self):
        self.head = None
        self.temp = None
        self.size = 0
 
    # Function which returns the size
    # of the Linked List
    def __len__(self):
        return self.size
 
    # Check the Linked List is
    # Empty or not
    def isempty(self):
        return self.size == 0
 
    # Responsible function to create
    # Linked List from Sparse Matrix
    def create_new_node(self, row, col, data):
 
        # Creating New Node
        newNode = Node(row, col, data, None)
 
        # Check whether the List is
        # empty or not
        if self.isempty():
            self.head = newNode
        else:
            self.temp.next = newNode
        self.temp = newNode
 
        # Incrementing the size
        self.size += 1
 
    # Function display the contents of
    # Linked List
    def PrintList(self):
        temp = r = s = self.head
        print("row_position:", end=" ")
        while temp != None:
            print(temp.row, end=" ")
            temp = temp.next
        print()
        print("column_postion:", end=" ")
        while r != None:
            print(r.col, end=" ")
            r = r.next
        print()
        print("Value:", end=" ")
        while s != None:
            print(s.data, end=" ")
            s = s.next
        print()
 
# Driver Code
if __name__ == "__main__":
 
    # Creating Object
    s = Sparse()
 
    # Assuming 4x5 Sparse Matrix
    sparseMatric = [[0, 0, 3, 0, 4],
                    [0, 0, 5, 7, 0],
                    [0, 0, 0, 0, 0],
                    [0, 2, 6, 0, 0]]
    for i in range(4):
        for j in range(5):
 
            # Creating Linked List by only those
            # elements which are non-zero
            if sparseMatric[i][j] != 0:
                s.create_new_node(i, j, sparseMatric[i][j])
 
    # Printing the Linked List Representation
    # of the sparse matrix
    s.PrintList()