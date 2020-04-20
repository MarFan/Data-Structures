import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        # Add item to the end of the queue
        return DoublyLinkedList.add_to_head(value)

    def dequeue(self):
        # Remove first item from list and return a value
        value = DoublyLinkedList.remove_from_head(self)
        return value

    def len(self):
        # return the number it items in the queue
        return self.size