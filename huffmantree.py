import abc

# Huffman Tree Implementation

# Base Class
class HuffmanBaseNode(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def isleaf(self):
        pass

    @abc.abstractmethod
    def weight(self):
        pass


# Huffman Tree Node; Leaf class

class HuffmanLeafNode(HuffmanBaseNode):
    '''
        Leaf Node for a Huffman Tree

        Attributes
        
        char element
        int weight
    '''

    def __init__(self, element : str, weight : int) -> None:
        self.element = element
        self.weight = weight

    @property
    def element(self) -> str:
        return self._element
    

    def weight(self) -> int:
        return self.weight
    
    def isleaf(self) -> bool:
        return True
    

# Huffman Tree Node : Internal Node Class
    
class HuffmanInternalNode(HuffmanBaseNode):
    '''
        Internal Node for Huffman Tree

        Attributes

        HuffmanBaseNode - left
        HuffmanBaseNode - right
        int - weight
    '''

    def __init__(self, left : HuffmanBaseNode, right : HuffmanBaseNode, weight : int) -> None:
        self.left = left
        self.right = right
        self.weight = weight

    @property
    def left(self) -> HuffmanBaseNode:
        return self._left
    
    @property
    def right(self) -> HuffmanBaseNode:
        return self._right
    
    def weight(self) -> int:
        return self.weight
    
    def isleaf(self) -> bool:
        return False
    

# Huffman Tree
    
class HuffmanTree:
    '''
        Class to Implement the Huffman Tree
    '''

    def __init__(self, element : str, weight: int) -> None:
        self.root = HuffmanLeafNode(element=element, weight=weight)

    def __init__(self, l : HuffmanBaseNode, r : HuffmanBaseNode, wt : int) -> None:
        self.root = HuffmanInternalNode(left=l, right=r, weight=wt)

    @property
    def root(self):
        return self._root
    
    def weight(self):
        return self.root.weight()
    
    def __eq__(self, otherTree: object) -> bool:
        return self.weight() == otherTree.weight()
    
    def __lt__(self, otherTree: object):
        return self.weight() < otherTree.weight()
        
    def __gt__(self, otherTree: object):
        return self.weight() > otherTree.weight()