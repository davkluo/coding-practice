class LinkedListNode:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_at_end(self, node: LinkedListNode):
        node.next = None

        if self.tail: # append to tail
            self.tail.next = node
            node.prev = self.tail
        else: # list was empty previously
            self.head = node
        
        self.tail = node
        self.length += 1
    
    def remove_at_head(self) -> LinkedListNode:
        if not self.head:
            return
        
        removed = self.head
        self.head = self.head.next

        if self.head:
            self.head.prev = None
        else: # list is now empty
            self.tail = None
        
        self.length -= 1

        return removed
    
    def shift_to_end(self, node):
        if not node.prev: # removing head
            self.remove_at_head()
        else:
            node.prev.next = node.next
            self.length -= 1
            if not node.next: # removing tail
                self.tail = node.prev
            else:
                node.next.prev = node.prev

        self.insert_at_end(node)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linked_list = DoublyLinkedList()
        self.node_map: dict[int, LinkedListNode] = {}

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1

        node = self.node_map[key]
        self.linked_list.shift_to_end(node)   

        return node.val

    def put(self, key: int, value: int) -> None:
        # Update only
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.linked_list.shift_to_end(node)
            return
        
        # New entry
        if self.linked_list.length == self.capacity:
            removed = self.linked_list.remove_at_head()
            del self.node_map[removed.key]

        node = LinkedListNode(key, value)
        self.node_map[key] = node
        self.linked_list.insert_at_end(node)


if __name__ == "__main__":
    # Basic get/put
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    assert cache.get(3) == -1  # key not found

    # Eviction of LRU key
    cache.put(3, 3)            # evicts key 2 (LRU)
    assert cache.get(2) == -1
    assert cache.get(3) == 3

    # Get refreshes recency
    cache2 = LRUCache(2)
    cache2.put(1, 1)
    cache2.put(2, 2)
    cache2.get(1)              # key 1 is now most recently used
    cache2.put(3, 3)           # evicts key 2 (LRU), not key 1
    assert cache2.get(2) == -1
    assert cache2.get(1) == 1

    # Put updates existing key value
    cache3 = LRUCache(2)
    cache3.put(1, 1)
    cache3.put(1, 10)
    assert cache3.get(1) == 10

    # Put on existing key refreshes recency
    cache4 = LRUCache(2)
    cache4.put(1, 1)
    cache4.put(2, 2)
    cache4.put(1, 10)          # updates key 1, now key 2 is LRU
    cache4.put(3, 3)           # evicts key 2
    assert cache4.get(2) == -1
    assert cache4.get(1) == 10
    assert cache4.get(3) == 3

    # Capacity of 1
    cache5 = LRUCache(1)
    cache5.put(1, 1)
    assert cache5.get(1) == 1
    cache5.put(2, 2)           # evicts key 1
    assert cache5.get(1) == -1
    assert cache5.get(2) == 2

    # LeetCode example
    cache6 = LRUCache(2)
    cache6.put(1, 1)
    cache6.put(2, 2)
    assert cache6.get(1) == 1
    cache6.put(3, 3)
    assert cache6.get(2) == -1
    cache6.put(4, 4)
    assert cache6.get(1) == -1
    assert cache6.get(3) == 3
    assert cache6.get(4) == 4

    cache7 = LRUCache(2)
    cache7.put(2, 1)
    cache7.put(3, 2)
    assert cache7.get(3) == 2
    assert cache7.get(2) == 1
    cache7.put(4, 3)
    assert cache7.get(2) == 1
    assert cache7.get(3) == -1
    assert cache7.get(4) == 3

    print("All tests passed.")