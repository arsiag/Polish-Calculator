__author__ = 'arsia'

import operator


class Node:
    left = None
    right = None

    def __init__(self, val):
        self.val = val
        # self.left = None
        # self.right = None


class ExpressionTree:

    def __init__(self):
        self.root = None
        self.ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "^": operator.pow}

    def setExpression(self, str):
        expressionList = str.split(" ")
        self.makeTree(expressionList)

    def is_float(self, input):
        try:
            num = float(input)
        except ValueError:
            return False
        return True

    def is_int(self, input):
        try:
            num = int(input)
        except ValueError:
            return False
        return True

    def makeTree(self, mylist):
        myStack = []
        for c in range(len(mylist)):
            if self.is_int(mylist[c]):
            #if mylist[c].isdigit():   (not good for floats)
                #print("AN INT")
                newnode = Node(int(mylist[c]))
                newnode.left = None
                newnode.right = None
                myStack.insert(0, newnode)
            elif self.is_float(mylist[c]):
                #print("A FLOAT")
                newnode = Node(float(mylist[c]))
                newnode.left = None
                newnode.right = None
                myStack.insert(0, newnode)
            else:
                #print("A SIGN")
                newnode = Node(mylist[c])
                newnode.left = myStack.pop(0)
                newnode.right = myStack.pop(0)
                myStack.insert(0 , newnode)
        self.root = myStack[0]

    def printRoot(self):
        print("Root is: " + str(self.root.val))

    # BFT ##############################################################################################################
    def printLevelOrder(self):
        print("This is Level Order Traversal (BFS):")
        myqueue = []
        myqueue.append(self.root)
        current = myqueue.pop(0)
        while current:
            print(str(current.val), end=' ')
            if current.left:
                myqueue.append(current.left)
            if current.right:
                myqueue.append(current.right)
            if myqueue:
                current = myqueue.pop(0)
            else:
                current = None
        print()

    # DFS ##############################################################################################################
    def printInOrder(self):
        print("This is In Order Traversal (DFS):")
        self.printInOrderHelper(self.root)
        print()

    def printInOrderHelper(self, node):
        if node.left:
            print("(", end=' ')
            self.printInOrderHelper(node.left)
        print(str(node.val), end=' ')
        if node.right:
            self.printInOrderHelper(node.right)
            print(")", end=' ')

    # DFS ##############################################################################################################
    def printPostOrder(self):
        print("This is Post Order Traversal (DFS):")
        self.printPostOrderHelper(self.root)
        print()

    def printPostOrderHelper(self, node):
        if node.left:
            print("(", end=' ')
            self.printPostOrderHelper(node.left)
        if node.right:
            self.printPostOrderHelper(node.right)
            print(")", end=' ')
        print(str(node.val), end=' ')

    # DFS ##############################################################################################################
    def printPreOrder(self):
        print("This is Pre Order Traversal (DFS):")
        self.printPreOrderHelper(self.root)
        print()

    def printPreOrderHelper(self, node):
        print(str(node.val), end=' ')
        if node.left:
            print("(", end=' ')
            self.printPreOrderHelper(node.left)
        if node.right:
            self.printPreOrderHelper(node.right)
            print(")", end=' ')

    # DFS ##############################################################################################################
    def getHeight(self):
        print("This is Height:")
        print("Max Height: " + str(1 + self.getHeightHelper(self.root)))

    def getHeightHelper(self, node):
        leftHeight = 0
        rightHeight = 0
        if node.left:
            leftHeight = 1 + self.getHeightHelper(node.left)
        if node.right:
            rightHeight = 1 + self.getHeightHelper(node.right)
        # print("Node " + str(node.val) + " Left vs right: " + str(leftHeight) + " " + str(rightHeight))
        if leftHeight > rightHeight:
            return leftHeight
        return rightHeight

    # DFS ##############################################################################################################
    def getDepth(self):
        print("This is Depth:")
        self.getDepthHelper(self.root, 0)

    def getDepthHelper(self, node, depth):
        print("Node {0:3} has depth of {1}".format(str(node.val), str(depth)))
        #print("Node " + str(node.val) + " depth: " + str(depth))
        if node.left:
            self.getDepthHelper(node.left, depth+1)
        if node.right:
            self.getDepthHelper(node.right, depth+1)


    def evaluate(self):
        print("The result of evaluation is: " + str(self.evaluateHelper(self.root)))

    def evaluateHelper(self, node):
        if self.is_int(node.val) or self.is_float(node.val):
            return node.val
        leftres = self.evaluateHelper(node.left)
        rightres = self.evaluateHelper(node.right)
        #print("Op is: " + node.val)
        #print("Left : " + str(leftres))
        #print("rigt : " + str(rightres))
        return self.ops[str(node.val)](leftres, rightres)



'''

              "-"
         /           \
       "*"           "+"
     /     \       /      \
    5      4.8   "/"      "+"
                /    \   /   \
               40    20 2     1

((5 * 4.8) - ((40 / 20) + (2 + 1)))
'''
myexpression1 = "1 2 + 20 40 / + 4.8 5 * -"
myexpression2 = "5 11 2 + 4.5 * + 363.50 -"

etree = ExpressionTree()
etree.setExpression(myexpression1)
#etree.printRoot()
etree.getHeight()
etree.getDepth()
etree.printLevelOrder()
etree.printInOrder()
etree.printPostOrder()
etree.printPreOrder()
etree.evaluate()


etree.setExpression(myexpression2)
#etree.printRoot()
etree.getHeight()
etree.getDepth()
etree.printLevelOrder()
etree.printInOrder()
etree.printPostOrder()
etree.printPreOrder()
etree.evaluate()





