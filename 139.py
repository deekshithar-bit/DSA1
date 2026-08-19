class TrieNode: #Trie Implementation and Advanced Operations
    def __init__(self):
        self.children = {}
        self.endsWith = 0
        self.prefixCount = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]
            node.prefixCount += 1

        node.endsWith += 1

    def countWordsEqualTo(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                return 0

            node = node.children[ch]

        return node.endsWith

    def countWordsStartingWith(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return 0

            node = node.children[ch]

        return node.prefixCount

    def erase(self, word):
        # Word doesn't exist
        if self.countWordsEqualTo(word) == 0:
            return

        node = self.root

        for ch in word:
            node = node.children[ch]
            node.prefixCount -= 1

        node.endsWith -= 1

trie = Trie()

trie.insert("apple")
print(trie.countWordsEqualTo("apple"))       # 1

trie.insert("app")
print(trie.countWordsStartingWith("app"))    # 2

trie.erase("app")
print(trie.countWordsStartingWith("app"))    # 1     