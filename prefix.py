
import pdb
import requests
import json
import heapq

#Multiway Trie implementation SIMILAR to the one in:
#   http://pythonfiddle.com/python-trie-implementation/
#BUT with a few changes to fit the challenge
#Added member variables:
#       MultiwayTrie: exclude used to keep from adding the prefix in the trie
#       Node: position used end up keeping order of the array
#Added class function:
#       get_all_without_prefix
########################################################################
class Node:

    def __init__(self, ch ):
        self.flag = False
        self.children = {}#size of alphabet
        self.position = 0#position in original array
        self.char = ch

class MultiwayTrie:

    def __init__(self, prefix):
        self.root = Node( '0' )
        self.exclude = None
        self.insert(prefix, -1)

        #gets the node that flags when to exclude the word in the array
        self.exclude = self.root
        for letter in prefix:
            self.exclude = self.exclude.children[ letter ]

    def insert(self, word, pos):

        curr_node = self.root
        for i in range (0, len(word)):
            if word[i] not in curr_node.children:
                curr_node.children[ word[i] ] = Node( word[i] )

            curr_node = curr_node.children[ word[i] ]

            #if this condition is true, then the word has the prefix we
            #want to exclude, therefore we will not insert the rest
            if curr_node == self.exclude:
                break

        curr_node.position = pos
        curr_node.flag = True



########################################################################
    #METHOD: dfs
    #Parameters:
    #   node = the node we are currently on
    #   pq = the priority queue to sort the words into 'array's order'
    #   word = the word we are constructing as we are going down
    def dfs( self, node, pq, word ):
        if node.char != '0':
            word += node.char
        for child in node.children:
            self.dfs( node.children[child], pq, word )

        if node.flag and node != self.exclude:
            heapq.heappush(pq, (node.position, word) )


    #My method implementation using the Trie data structure
    def get_all_without_prefix( self, array, ):
        #we do a dfs for all the nodes and add the word into priority_queue
        #to keep the ordering of the original array
        #
        pq = []#priority queue
        word = ""
        self.dfs( self.root, pq=pq, word=word )
        return pq


###########################################################################
###########################################################################
###########################################################################
###########################################################################


TOKEN = 'c6472b388a029564c0702d72f4730594'
URL = "http://challenge.code2040.org/api/prefix"
VALIDATION = 'http://challenge.code2040.org/api/prefix/validate'

r = requests.post(URL, json={'token':TOKEN}, headers={'Content-Type':'application/json'})

dictionary = json.loads(r.text)

prefix = dictionary['prefix']
array = dictionary['array']

trie = MultiwayTrie( prefix )

i = 0
for words in array:
    trie.insert(words, i)
    i +=1

pq = trie.get_all_without_prefix( array )

toReturn = [None] * len(pq)

for i in range( 0, len(pq)):
    toReturn[i] = heapq.heappop(pq)[1]

r2 = requests.post(VALIDATION, json={'token':TOKEN, 'array':toReturn })


