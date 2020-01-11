from trieNode import TrieNode

class Trie(object):

    # Constructor for objects of type Trie
    def __init__(self):
        self.root = TrieNode()


    # Adds an entire word to tree
    def addWord(self, exp):
        i = 0
        localRoot = self.root
        # traverses tree while the char sequence exists in tree
        while i < (len(exp)) and exp[i] in localRoot.children:
            localRoot = localRoot.children[exp[i]]              # get next character
            i += 1
        # adds the remaining chars to tree
        while i < (len(exp)):
            localRoot.addChild(exp[i])              # add child
            localRoot = localRoot.children[exp[i]]  # set root to newly added child
            i += 1
        # set the word of this final node
        localRoot.setWord(exp)


    # Returns True if word exists in tree, else False
    def contains(self, exp):
        i = 0
        localRoot = self.root

        for i in range(len(exp) - 1):
            if exp[i] in localRoot.children.keys():
                localRoot = localRoot.children[exp[i]]
            else:
                return False
        return True


    # Returns list of words that begin with the passed Prefix
    def get_prefix(self, prefix):
        i = 0
        localRoot = self.root
        words = []                  # list stores Nodes that follow

        # Gets the node representing the last letter in prefix
        for i in range(len(prefix)):
            if prefix[i] in localRoot.children.keys():
                localRoot = localRoot.children[prefix[i]]
            else:
                return words

        # Get list of children nodes of this prefix
        if localRoot == self.root:
            childNodes = [node for node in localRoot.children.values()]
        else:
            childNodes = [localRoot]

        # While items (children) remain, append the expressions to words list
        while childNodes:
            this_node = childNodes.pop()
            if this_node.word != None:
                words.append(this_node.word)

            childNodes = [node for node in this_node.children.values()] + childNodes

        return words
