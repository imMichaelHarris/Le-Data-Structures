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
        self.list = DoublyLinkedList()
        self.cache = {}
        self.limit = limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.list.move_to_end(node)
            # print(f"This is the value {node[key]}, {key}")
            # self.list.delete(node)
            # self.list.add_to_head(node)
            # print("test", node[1])
            return node.value[1]
        else:
            return None
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
        pair = (key, value)
        # print("Hey ", pair)
        # Add pair to dll
        # self.cache[key] = pair
        # If cache is at max capacity
        # print(F"Hi {self.list.head.value}")
        if key in self.cache:
            node = self.cache[key]
            node.value = pair
            print(f"Front {self.list.head}")
            self.list.move_to_end(node)
            # self.cache[key] = pair
            return
            # print(self.cache[key], pair)
            # node.value = pair
            # self.list.move_to_front(self.cache[key])
            # node[key] = value
            # self.list.add_to_head(pair)
        elif len(self.list) >= self.limit:
            print("Over", len(self.list))
            del self.cache[self.list.head.value[0]]
            self.list.remove_from_head()


        
        self.list.add_to_tail(pair)
        self.cache[key] = self.list.tail

        # If key already exist in cache overwrite the value