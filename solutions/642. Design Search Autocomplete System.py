#Solution 1
class AutocompleteSystem:
    #Approach: Trie + HashMap + Constant-time sorting
    #Time Complexity: O(n * l) for init; O(n) for input
    #Space Complexity: O(n * l)
    #where, n is the total number of sentences and l is the average length of a sentence
    #and, m is the current length of the input
    #and, p is the size of prefixMap at the current TrieNode
    
    def __init__(self, sentences: List[str], times: List[int]):
        self.map = {}
        self.root = TrieNode()
        self.input_sb = []
        
        for i in range(len(sentences)):
            self.map[sentences[i]] = self.map.get(sentences[i], 0) + times[i]
            self.insert(sentences[i])
            
    def insert(self, sentence):
        curr = self.root
        for char in sentence:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            
            #adding the sentence if not already in top3 && updating the pair objects
            temp = set([i.sentence for i in curr.top3])
            temp.add(sentence)
            curr.top3 = [Pair(self.map[i], i) for i in temp]
            curr.top3.sort(reverse=True)
            curr.top3 = curr.top3[:3]
        
    def search(self, input_sb):
        curr = self.root
        for char in input_sb:
            if char not in curr.children:
                return {}
            curr = curr.children[char]
        
        return curr.top3
​
    def input(self, c: str) -> List[str]:
        if c == '#':
            input_str = ''.join(self.input_sb)
            self.map[input_str] = self.map.get(input_str, 0) + 1
            self.insert(input_str)
            self.input_sb = []
            return
            
        self.input_sb.append(c)
        top3 = [i.sentence for i in self.search(self.input_sb)]
        return top3
​
class TrieNode:
    def __init__(self):
        self.top3 = []
        self.children = {}
    
#Solution 2
"""
class AutocompleteSystem:
    #Approach: Trie + HashMap + Min Heap
    #Time Complexity: O(n * l) for init; O(n * m) for input, but average case is much better
    #Space Complexity: O(n^2 * l)
    #where, n is the total number of sentences and l is the average length of a sentence
    #and, m is the current length of the input
    
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.input_sb = []
        
        for i in range(len(sentences)):
            self.insert(sentences[i], times[i])
            
    def insert(self, sentence, times):
        curr = self.root
        for char in sentence:
