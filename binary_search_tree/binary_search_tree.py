import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


# class BinarySearchTreeNode:
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # recursive `insert` implementation
    # def insert(self, value):
    #     # base case: we found a parking spot!
    #     # we're in an empty spot in the tree
    #     if self is None:
    #         self = BinarySearchTreeNode(value)
    #     # if we aren't at a base case,  move towards it
    #     else:
    #         # self is a node with a value
    #         # compare the value to the value at this node
    #         if value < self.value:
    #             # move to the left
    #             self.left.insert(value)
    #         # otherwise, value >= self.value
    #         else:
    #             self.right.insert(value)

    def insert(self, value):
        # self.left and/or self.right need to be valid nodes
        # for us to call `insert` on them
        if value < self.value:
            # check if self.left is a valid node
            if self.left:
                self.left.insert(value)
            # the left side is empty
            else:
                # we've found a valid parking spot
                self.left = BinarySearchTree(value)

        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        else:
            if target > self.value:
                if self.right:
                    return self.right.contains(target)

            if target < self.value:
                if self.left:
                    return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        current_max = self.value
        
        # while self:
        #     print(current_max, self.value)
        #     if current_max < self.value:
        #         current_max = self.value
        #     self = self.right

        while self.right:
            current_max = self.right.value
            self = self.right

        return current_max        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value) # first callback on value

        # if not self.left and not self.right:
        #     return

        # if self:
        if self.left:
            # cb(self.value)
            self.left.for_each(cb)
            # check_again(self.left, cb)

        if self.right:
            # cb(self.value)
            self.right.for_each(cb)
            # check_again(self.right, cb)

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
