class LRUCache:

    def __init__(self, capacity: int):
        self.start, self.end = Node(-1, -1), Node(-1, -1)
        self.start.next, self.end.prev = self.end, self.start
        self.limit = capacity
        self.d : dict[int, Node] = {}

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        n = self.d[key]
        self.delete(n)
        self.add(n)

        return n.value

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.delete(self.d[key])
        n = Node(key, value)
        self.add(n)
        self.d[key] = n

        if len(self.d) > self.limit:
            n_d = self.start.next
            self.delete(n_d)
            del self.d[n_d.k]
    
    def add(self, n: Node):
        n.next = self.end
        prev = self.end.prev
        self.end.prev = n
        n.prev = prev
        prev.next = n
    
    def delete(self, n: Node):
        n.prev.next, n.next.prev = n.next, n.prev

class Node:
    def __init__(self, key: int, val: int):
        self.prev = None
        self.next = None
        self.k = key
        self.value = val