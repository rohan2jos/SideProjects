from HeapNode import *
#from queue import *

class BinTree:


    '''
    a root by itself is a node, initialize it to null when the object of BinTree is created
    '''
    root = None

    def __init__(self, name):
        print "[BinTree.__init__] entered the BinTree class with instance name:: ", name

    '''
    insert()
    args: Integer data
    returns: nothing
    The function checks if the root node is empty and if it is, sets this data
    to the root node
    if the root node is not empty, it will call add() with the root and the data
    '''
    def insert(self, data):
        if self.root == None:
            newnode = HeapNode(data, 0, 0)
            self.root = newnode
        else:
            self.root = self.add(self.root, data)
            temp = self.root.left


    '''
    add()
    args: root, Integer data
    returns: the root with the data assigned to a node and added to the tree
    '''
    def add(self, node, data):
        if node.data < data:
            '''
            recursion: step 1: breaking condition
            '''
            if node.right is None:
                print "adding " + str(data) + " as right to " + str(node.data)
                node.right = HeapNode(data, None, None)
            else:
                '''
                recursion: step 2: call recursion with right node of the current node
                '''
                self.add(node.right, data)
        else:
            '''
            recursion: step 1: breaking condition
            '''
            if node.left is None:
                print "adding " + str(data) + " as left to " + str(node.data)
                node.left = HeapNode(data, None, None)
            else:
                '''
                recursion: step 2: call recursion with left node of the current node
                '''
                self.add(node.left, data)
        return node

    '''
    traversal()
    args: String type that indicates the type of traversal
    returns: nothing
    calls the respective methods that pertain to the traversal
    prints the array of traversed nodes
    '''
    def traversal(self, type):
        traversedNodes = []
        if type == "inorder":
            print "[BinTree.traversal()] got command for inorder traversal"
            return self.inorder(self.root, traversedNodes)
        elif type == "preorder":
            print "[BinTree.traversal()] got command for preorder traversal"
            return self.preorder(self.root, traversedNodes)
        else:
            print "[BinTree.traversal()] got command for postorder traversal"
            return self.postorder(self.root, traversedNodes)


    '''
    inorder()
    args: root node, empty array
    returns: the array with the nodes inorder
    takes the root node and then recursively traverses inorder, adding the visited nodes
    to the empty array and returns that array
    '''
    def inorder(self, node, traversedNodes):

        print "[BinTree.inorder()] entered inorder traversal"

        if node:
            self.inorder(node.left, traversedNodes)
            traversedNodes.append(node.data)
            self.inorder(node.right, traversedNodes)
        return traversedNodes

    '''
    preorder()
    args: root node, empty array
    returns: the array with the nodes preorder
    takes the root node and then recursively traverses preorder, adding the visited nodes
    to the empty array and returns that array
    '''
    def preorder(self, node, traversedNodes):

        print "[BinTree.preorder()] entered preorder traversal"

        if node:
            traversedNodes.append(node.data)
            self.preorder(node.left, traversedNodes)
            self.preorder(node.right, traversedNodes)

        return traversedNodes

    '''
    postorder()
    args: root node, empty array
    returns: the array with the nodes postorder
    takes the root node and then recursively traverses postorder, adding the visited nodes
    to the empty array and returns that array
    '''
    def postorder(self, node, traversedNodes):

        print "[BinTree.postorder()] entered postorder traversal"

        if node:
            self.postorder(node.left, traversedNodes)
            self.postorder(node.right, traversedNodes)
            traversedNodes.append(node.data)

        return traversedNodes

    '''
    depth()
    args: none
    returns: nothing
    prints the max depth of the tree
    '''
    def depth(self):
        print "[BinTree.depth()] finding depth of tree"
        d = self.max_depth(self.root)
        print "depth (not 0 indexed) of tree is :: ", d
        print "depth (0 indexed) of tree is :: ", d - 1

    '''
    max_depth()
    args: the root node (current node in the case of recursion)
    returns: the maximum depth of the tree
    '''
    def max_depth(self, node):

        '''
        recursion: step 1: breaking condition
        '''
        if node is None:
            return 0
        else:
            '''
            recursion: step 2: recurse with left first and then right
            '''
            ldepth = self.max_depth(node.left)
            rdepth = self.max_depth(node.right)


        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth + 1


    '''
    level_wise()
    args: node
    returns: nothing
    calls the method that traverses the tree and prints the nodes according to the level
    '''
    def level_wise(self):
        print "[BinTree.level_wise()] starting level wise printing"


        '''
        calling the method that prints level wise
        '''
        self.level_print(self.root, [])
        return self.level_print(self.root, [])


    '''
    level_print()
    args: root node, empty list
    returns: nothing
    Prints the tree according to the level

    Sample output:


     root node
       5
     level 2
       3      9
     level 3
       1      8
     level 4
       6

    '''
    def level_print(self, node, queue):
        finalstr = "  "
        if node is None:
            return
        levelpointer = 1

        queue.append(node)

        while len(queue) != 0:
            level = len(queue)
            if levelpointer == 1:
                finalstr = finalstr + "\n root node " + "\n"
            else:
                finalstr = finalstr + "\n level " + str(levelpointer) + "\n"
            while level != 0:
                n = queue.pop(0)
                finalstr = finalstr + "   " + str(n.data)

                if n.left != None:
                    queue.append(n.left)
                finalstr = finalstr + "   "
                if n.right != None:
                    queue.append(n.right)

                level = level - 1
            levelpointer = levelpointer + 1

        print finalstr
        return finalstr




instance = BinTree("instance")
instance.insert(5)
instance.insert(3)
instance.insert(9)
instance.insert(8)
instance.insert(6)
instance.insert(1)
instance.traversal("inorder")
instance.traversal("preorder")
instance.traversal("postorder")
#print instance.root.data
#print instance.root.left.data
#print instance.root.right.data
#print instance.root.right.left.data
#instance.insert(9)
#instance.print_root()
instance.depth()
instance.level_wise()