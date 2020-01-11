from trie import Trie
from trieNode import TrieNode
import re
import os.path
from os import path

def main():
    # Trie allows us to retrieve all words beginning with the designated prefix
    wordTrie = Trie()
    instances = {}

    # get file name from user and open for reading
    filename = input("Please enter file to be indexed (be sure to include .txt extension): ")
    while not path.exists(filename):
        print("File does not exist.")
        filename = input("Please enter file to be indexed (be sure to include .txt extension): ")
    file = open(filename, "r")

    # read words from file, recording their position along the way
    line_num = 1
    for line in file:
        word_num = 1
        for word in line.split():
            # use regex to convert all words to lowercase and remove special chars
            word = re.sub(r'[^a-zA-Z-]', "", word.lower())
            # store word in trie
            wordTrie.addWord(word)
            # store the instances of word
            if word in instances:
                instances[word].append(str(line_num) + "-" + str(word_num))
            else:
                instances[word] = []
                instances[word].append(str(line_num) + "-" + str(word_num))
            word_num += 1
        line_num += 1

    # allow user to search for desired prefix, printing all words beginning with entered prefix
    while True:
        pre = input("Please enter prefix of word, or entire word, you'd like to search for (Ctrl + C to quit): ")
        words = wordTrie.get_prefix(pre)
        if not words:
            print("There are no words beginning with", pre, "- Please try again.")
        else:
            for item in words:
                print(item, str(instances[item]))

if __name__ == "__main__":
    main()
