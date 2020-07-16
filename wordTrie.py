'''
Caveat: The final tag must be added. It is absent here.
'''

class wordTrie:

    def __init__(self, words: list):
        self.words = words
        self.root = dict()

    def buildTrie(self):
        for word in self.words:
            self.addWord(word)

    def addWord(self, word: str):
        
        if word not in self.words:
            self.words.append(word)

        level = self.root
        
        for letter in word:
            if letter not in level:
                level[letter] = dict()

            level = level[letter]

    def checkWord(self, word: str):
        
        level = self.root
        
        for letter in word:
            if letter in level:
                level = level[letter]
            else:
                print(f'The word "{word}" does not exist!')
                return None
        print(f'The word "{word}" exists!')
        return word


    def listWords(self):
        print(self.words)


def test1():
    trie = wordTrie(['kerem', 'ahmet'])
    trie.buildTrie()
    trie.addWord('zeynep')

    trie.checkWord('kerem')
    trie.checkWord('kerm')

test1()
