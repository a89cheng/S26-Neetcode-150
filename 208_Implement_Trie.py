# Completed May, 30 2026 | 50 minutes

class TrieNode():
    def __init__(self, letter=None):
        self.letter = letter
        self.next = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for idx in range(len(word)):
            if word[idx] not in current.next:
                current.next[word[idx]] = TrieNode(word[idx])
            current = current.next[word[idx]]
        current.next[None] = None

    def search(self, word: str) -> bool:
        current = self.root
        for idx in range(len(word)):
            if word[idx] not in current.next:
                return False
            current = current.next[word[idx]]
        if None in current.next:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for idx in range(len(prefix)):
            if prefix[idx] not in current.next:
                return False
            current = current.next[prefix[idx]]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

