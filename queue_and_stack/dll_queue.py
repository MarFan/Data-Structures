import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # Add item to the end of the queue
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        # Remove first item from list and return a value
        if self.size == 0:
            return None

        self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        # return the number it items in the queue
        return self.size