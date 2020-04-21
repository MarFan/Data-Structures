import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = DoublyLinkedList()
        self.cache = dict() # cache

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.cache:
            return None

        node = self.cache[key]
        self.storage.move_to_front(node)
        return node.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # is the item in storage already
        if key in self.cache:
            node = self.cache[key]
            node.value = (key, value)
            self.storage.move_to_front(node)
            return
            # self.cache[key] =  # update value in cache

        # has the limit been reached
        if self.size >= self.limit:
            # remove last node
            del self.cache[self.storage.tail.value[0]]
            self.storage.remove_from_tail()
            self.size -= 1
        
        # if not in cache or limit reached add a new entry
        self.storage.add_to_head((key, value)) # adds to dbll
        self.cache[key] = self.storage.head # adds to dict for
        self.size += 1