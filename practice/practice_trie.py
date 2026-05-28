"""
Exercise 1 — LeetCode #208 Implement Trie (Prefix Tree)

Implement a Trie with insert, search, and startsWith.

trie = Trie()
trie.insert("apple")
trie.search("apple")    → True
trie.search("app")      → False
trie.startsWith("app")  → True
trie.insert("app")
trie.search("app")      → True

time: O(n) per op  space: O(n)
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True 

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


"""
Exercise 2 — LeetCode #211 Design Add and Search Words

Same as Trie but search supports '.' as wildcard (matches any letter).

obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.search("pad") → False
obj.search("bad") → True
obj.search(".ad") → True
obj.search("b..") → True

time: O(n) insert, O(26^n) worst case search  space: O(n)
"""
class WordDictionary:
    def __init__(self):
        pass

    def addWord(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass
