class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

def get_valid_t9_words(number: str, words: list[str]) -> list[str]:
    t9_mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    trie = Trie()

    for word in words:
        trie.insert(word)

    result = []

    def percorre_trie(node, index, path):
        if index == len(number):
            if node.is_word:
                result.append(path)
            return
        digit = number[index]
        for char in t9_mapping.get(digit, ''):
            if char in node.children:
                percorre_trie(node.children[char], index + 1, path + char)

    percorre_trie(trie.root, 0, '')
    return result

print(get_valid_t9_words("4663", ["c", "good", "home", "gone", "food", "hello"]))
