class PrefixTree:

    def __init__(self):
        self.root_node = Node()

    def insert(self, word: str) -> None:
        curr = self.root_node
        for letter in word:
            if letter not in curr.d:
                curr.d[letter] = Node()
            curr = curr.d[letter]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root_node
        for letter in word:
            if letter not in curr.d:
                return False
            curr = curr.d[letter]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root_node
        for letter in prefix:
            if letter not in curr.d:
                return False
            curr = curr.d[letter]
        return True

class Node:
    def __init__(self):
        self.d:dict[str, Node] = defaultdict(Node)
        self.is_word = False
      
        