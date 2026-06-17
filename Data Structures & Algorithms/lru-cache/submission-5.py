# The strategy is to have
# 1. Doubly linked list with fixed size, this to ensure easy getting of tails and heads (least and most used)
# 2. Key value map, key = key, value = node in linked list
# 
# When we get, we get on map, then return the val of node
# Then if node != heads, we make it head
# 
# When we put
# If exists, update in place then move to head
# If not exists, add on head
# If exceed capacity, remove tail then add on head
# 
# No deletion so no need to think about it

class Node: 
    def __init__(self, key: int, val: int, prev: Node | None, next: Node | None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next 

class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.record = {} # Map of key to node
        self.capacity = capacity
    
    def moveToHead(self, node: Node) -> None:
        # If node already head, we dont do nothing
        if self.head == node:
            return 

        # If node is tail, we should record first the new tail
        if node == self.tail:
            self.tail = self.tail.next

        # We move it to head
        # Lets first remove it
        # if it has prev, then prev next should be node next
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        # now we can safely move it forward
        if self.head:
            self.head.next = node
            node.prev = self.head
            
        self.head = node

        # If self.tail none, meaning theres only one node 
        if not self.tail:
            self.tail = node


    def get(self, key: int) -> int:
        if not key in self.record:
            return -1
        
        # We get the value (node)
        node = self.record[key]
        result = node.val

        self.moveToHead(node)

        return result        

    def put(self, key: int, value: int) -> None:
        if key in self.record:
            node = self.record[key]
            node.val = value

            self.moveToHead(node)
        else:
            # We create new, add to head
            node = Node(key, value, None, None)
            self.record[key] = node
            self.moveToHead(node)

            # We check for capacity
            if len(self.record) > self.capacity:
                del self.record[self.tail.key]
                self.tail = self.tail.next

# n   1
# n   1 2
# n   1 2 3
# 1   2 3 1
# 2   3 1 2
# -1  3 1 2
# n   1 2 4
# 1   2 4 1
# 2   4 1 2
# -2  4 1 2
# 4   1 2 4
# 2   1 4 2
# n   4 2 1


        

