import heapq
def getName():
	return "", "Mohammed"

class MyHuffman():
    #static member
    # dictionay to hold the characters and their coressponding bitcode
    chars = {}
    def __init__(self):
        # Huffman tree Node
        self.tree = None
        # position in the bitstring being decoded
        self.decodePosition = 0

    def build(self, weights):
        # Build a huffman tree from the dictionary of character:value pairs
        heap = []
        for ch in weights:
            heapq.heappush(heap,Node(weights[ch],ch))
            
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            left.huff = 1
            right.huff = 0
            newNode = Node(left.freq+right.freq, left.data+right.data, left, right)
            heapq.heappush(heap,newNode)
            
        
        self.tree = heapq.heappop(heap)
        MyHuffman.makeLookupTable(self.tree)
    
    def makeLookupTable(node, val=''):
        newVal = val + str(node.huff)

        if(node.left):
            MyHuffman.makeLookupTable(node.left, newVal)
        if(node.right):
            MyHuffman.makeLookupTable(node.right, newVal)
 
        if(not node.left and not node.right):
            MyHuffman.chars[node.data] = newVal

        
        

    def encode(self, word):
        code = ''
        for ch in word:
            code += MyHuffman.chars[ch]
        return code

    def decode(self, bitstring):
        # Return the word encoded in bitstring, or None if the code is invalid
        node = self.tree
        ans = ''
        for i in bitstring:
            
            if node is None:
                return None
            if node.left is None and node.right is None:
                ans += str(node.data)
                node = self.tree
            if i == '0':
                node = node.right
            if i == '1':
                node = node.left
        return ans


    
    def recursiveTraverseTree(self, node, bitString):
        # Return the character after traversing the Huffman tree through the bitstring
        #node represent the tree node
        if node.left is None and node.right is None:
                return node.data
        
        if bitstring == '0':
            return (self.recursiveTraverseTree(node.right,bitString[1:]))
        if (bitstring == '1'):
            return (self.recursiveTraverseTree(node.left,bitString[1:]))
        
    
class Node:
    def __init__(self,freq,data,left=None,right=None):
        self.freq = freq

        self.data = data

        self.left = left

        self.right = right

        self.huff = ''
        def __lt__(self, other):
            return self.freq < other.freq

        def __le__(self, other):
            return self.freq <= other.freq

        def __gt__(self, other):
            return self.freq > other.freq

        def __ge__(self, other):
            return self.freq >= other.freq
        


   

