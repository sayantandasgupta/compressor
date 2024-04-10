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
        self.wt = weight

    @property
    def element(self) -> str:
        return self._element
    
    @element.setter
    def element(self, value):
        self._element = value
    

    def weight(self) -> int:
        return self.wt
    
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
        self.wt = weight

    @property
    def left(self) -> HuffmanBaseNode:
        return self._left
    
    @left.setter
    def left(self, value : HuffmanBaseNode):
        self._left = value
    
    @property
    def right(self) -> HuffmanBaseNode:
        return self._right
    
    @right.setter
    def right(self, value : HuffmanBaseNode):
        self._right = value
    
    def weight(self) -> int:
        return self.wt
    
    def isleaf(self) -> bool:
        return False
    

# Huffman Tree
    
class HuffmanTree:
    '''
        Class to Implement the Huffman Tree
    '''

    def __init__(self, *args) -> None:
        if len(args) == 2:
            element, weight = args
            self.root = HuffmanLeafNode(element=element, weight=weight)
        else:
            left, right, weight = args
            self.root = HuffmanInternalNode(left=left, right=right, weight=weight)

    @property
    def root(self):
        return self._root
    
    @root.setter
    def root(self, value):
        self._root = value
    
    def weight(self):
        return self.root.weight()
    
    def __eq__(self, otherTree: object) -> bool:
        return self.weight() == otherTree.weight()
    
    def __lt__(self, otherTree: object):
        return self.weight() < otherTree.weight()
        
    def __gt__(self, otherTree: object):
        return self.weight() > otherTree.weight()