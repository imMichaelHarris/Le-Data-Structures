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
        # print(self.value)
        if value < self.value:
            
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = newNode
        else:

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
        # print(self.value, target)
        if self.value is None:
            return False
        if self.value == target:
            return True
        else:
            if target < self.value:
                if self.left is None:
                    return None
                else:
                    return self.left.contains(target)
            else:
                if self.right is None:
                    return None

                return self.right.contains(target) 

    # Return the maximum value found in the tree
    def get_max(self):

        # Check if something on right if there is then call get max on right value
        # Base case when right is None then return self.value
        if self.right is None:
            return self.value
        return self.right.get_max()


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.value is None:
            return
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)
        return cb(self.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # If node value is none then return
        # Go left recursive
        # print value
        # Go right recursive
        if node is None:
            return
        if self.left is not None:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right is not None:
            self.right.in_order_print(self.right)

        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while queue.len() > 0:
            # pop node off queue
            # print node
            # add the left and right node in queue
            node = queue.dequeue()
            print(node.value)
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        # While stack not empty
            # pop off stack 
            # print node
            # iF there is a left push
            # If there is a right push
        while stack.len() > 0:
            node = stack.pop()
            print(node.value)
            if node.left is not None:
                stack.push(node.left)
            if node.right is not None:
                stack.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
