class TrieNode(object):

    """ each node contains a character and a list of its children
        params: char - the letter represented by TrieNode
                word - the word that is derived when traversing tree up to this node"""
    def __init__(self, char="*", word=None):
        self.char = char
        self.word = None
        self.children = {}


    # Allows Trie to access the children of this node
    def __getitem__(self, char):
        return self.children[char]


    # Returns word represented when reaching this node in Trie
    def getWord(self):
        return self.word


    # Sets word represented when reaching this node in Trie
    def setWord(self, word):
        self.word = word


    # Accepts a character as a parameter and adds it as a child to this node
    def addChild(self, char):
        if not char in self.children:         # execute if value is not already a child
            self.children[char] = TrieNode(char)
