import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        newNode = BinarySearchTree(value)
        # If the value inserting is less then go
        print(self.value)
        if value < self.value:
            print("less ", value, self.value)
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = newNode
        else:
            print("not")

            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = newNode
            

            # If the left value is not None then call
            # If none then set the left to value

        # Else go right

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #If the target is self.value then return
        # Otherwise check if target is less than value if so use recursion to go left
        # If target isnt less than the self.value than go use recursion to goright
        if self.value == target:
            return self.value

        if target < self.value:
            self.contains(self.left, target)
        else:
            self.contains(self.right, target) 

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
