class Node:
    def __init__(self, value, depth):
        self.value = value
        self.child = None
        self.depth = depth
    
    def findValue(self, value):
        if self.child == None:
            return None
        else:
            for node in self.child:
                if node.value == value:
                    return node
            return False
    
    def getLeafNum(self, depth):
        if self.child == None:
            return 0
        stack = [self]
        targetDepth = self.depth + depth
        num = 0
        while len(stack) != 0:
            node = stack.pop()
            if node.child == None:
                if node.depth == targetDepth:
                    num += 1
            else:
                for childNode in node.child:
                    stack.append(childNode)
                    if childNode.child == None and childNode.depth == targetDepth:
                        num += 1
        return num
            
class Tree:
    def __init__(self):
        self.root = Node(None, 0)


def solution(words, queries):
    answer = []
    tree = createTree(Tree(), words)
    reverseTree = createReverseTree(Tree(), words)
    for query in queries:
        if query[0] == "?":
            answer.append(checkTree(reverseTree, query[::-1]))
        else:
            answer.append(checkTree(tree, query))
    return answer

def createTree(tree, words):
    for word in words:
        n = len(word)
        node = tree.root
        for i in range(n):
            childNode = node.findValue(word[i])
            if childNode == None:
                node.child = [ Node(word[i], i+1) ]
            elif childNode == False:
                node.child.append(Node(word[i], i+1))
            else:
                node = childNode
    return tree

def createReverseTree(tree, words):
    for word in words:
        n = len(word)
        node = tree.root
        depth = 1
        for i in range(n-1, -1, -1):
            childNode = node.findValue(word[i])
            if childNode == None:
                node.child = [ Node(word[i], depth) ]
            elif childNode == False:
                node.child.append(Node(word[i], depth))
            else:
                node = childNode
            depth += 1
    return tree

def checkTree(tree, query):
    n = len(query)
    node = tree.root
    for i in range(n):
        if query[i] == "?":
            depthLeft = n - i
            return node.getLeafNum(depthLeft)
        else:
            childNode = node.findValue(query[i])
            if childNode == None or childNode == False:
                return 0
            else:
                node = childNode



print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
    