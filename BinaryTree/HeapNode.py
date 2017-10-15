'''
Class for the node that will be used in the heap
will be imported into the implementing program
'''

class HeapNode:

    data = 0
    left = ''
    right = ''

    '''
    __init__() --> constructor
    args: data, left node, right node
    returns: the initialized node with the passed arguments
    '''
    def __init__(self, data, left, right):
        print "[HeapNode.__init__()] initializing HeapNode with ", data
        self.data = data
        self.left = None
        self.right = None

    '''
    get_data()
    args: none
    returns: the data that is contained in this node
    '''
    def get_data(self):
        return self.data

    '''
    get_right()
    args: none
    returns: the right sub-node to this node.  Will return nothing if it is the leaf node
    '''
    def get_right(self):
        print "[HeapNode.get_right()] returning the right node of the current HeapNode"
        return self.right

    '''
    get_left()
    args: none
    returns: the left sub-node to this node. Will return nothing if it is the leaf node
    '''
    def get_left(self):
        print "[HeapNode.get_left()] returning the left node of the current HeapNode"
        return self.left

    '''
    set_data()
    args: Integer -> data
    returns: nothing
    Sets the data of this node to the data argument that was passed
    '''
    def set_data(self, data):
        print "[HeapNode.set_data] setting data of the HeapNode to ", data
        self.data = data

    '''
    set_right()
    args: HeapNode
    returns: nothing
    Sets the right sub-node of this node to the node that was passed
    '''
    def set_right(self, node):
        print "[HeapNode.set_right] setting the right node of " + str(self.data) + " to " + str(node.get_data())
        self.right = node

    '''
    set_left()
    args: HeapNode
    returns: nothing
    Sets the left sub-node of this node to the node that was passed
    '''
    def set_left(self, node):
        print "[HeapNode.set_left] setting the left node of " + str(self.data) + " to " + str(node.get_data())
        self.left = node
