class WordDictionary:

    def __init__(self):
        self.map = Node()

    def addWord(self, word: str) -> None:
        curr = self.map
        for c in word:
            if c not in curr.d:
                curr.d[c] = Node()
            curr = curr.d[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in curr.d.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.d:
                        return False
                    curr = curr.d[c]
            return curr.isWord
        return dfs(0, self.map)


class Node:
    def __init__(self):
        self.d: dict[char, Node] = defaultdict(Node)
        self.isWord = False
        
