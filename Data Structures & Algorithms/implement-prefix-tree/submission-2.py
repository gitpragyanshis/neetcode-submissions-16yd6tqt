class PrefixTree:

    def __init__(self):
        self.look_up = Node()
        
    def insert(self, word: str) -> None:
        curr = self.look_up

        for c in word:
            if c not in curr.map:
                curr.map[c] = Node()
            curr = curr.map[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.look_up
        for c in word:
            if c not in curr.map:
                return False
            curr = curr.map[c]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.look_up
        for c in prefix:
            if c not in curr.map:
                return False
            curr = curr.map[c]
        return True


class Node:
    def __init__(self):
        self.map: dict[char, Node] = defaultdict(Node)
        self.isWord = False
        
        