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
            print("pop 노드 ", node.value)
            if node.child == None:
                print("자식이 없는 노드", node.value)
                
            else:
                for childNode in node.child:
                    print(node.value, "의 자식 중 하나",childNode.value)
                    stack.append(childNode)
                    if childNode.child == None and childNode.depth == targetDepth:
                        print(childNode.value, "는 원하는 단어!")
                        num += 1
                        print("현재 갯수 : ", num)
        return num
            
class Tree:
    def __init__(self):
        self.root = Node(None, 0)


def solution(words, queries):
    answer = []
    tree = createTree(Tree(), words)
    reverseTree = createReverseTree(Tree(), words)
    BFS(tree)
    for query in queries:
        print('-------', query)
        if query[0] == "?":
            answer.append(checkTree(reverseTree, query[::-1]))
        else:
            answer.append(checkTree(tree, query))
    return answer

def createTree(tree, words):
    for word in words:
        print(word, "를 트리에 추가")
        n = len(word)
        node = tree.root
        for i in range(n):
            print("깊이 :", i+1, "단어 : ", word[i])
            childNode = node.findValue(word[i])
            if childNode == None:
                print("자식 노드가 1개도 없었음")
                node.child = [ Node(word[i], i+1) ]
                node = node.child[0]
            elif childNode == False:
                print("자식 노드 리스트에 찾고자하는 값 없음")
                newNode = Node(word[i], i+1)
                node.child.append(newNode)
                node = newNode
            else:
                print("자식 노드 중 발견")
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
                node = node.child[0]
            elif childNode == False:
                newNode = Node(word[i], depth)
                node.child.append(newNode)
                node = newNode
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

def BFS(tree):
    from collections import deque
    node = tree.root
    queue = deque([node])
    while len(queue) != 0:
        node = queue.popleft()
        if node.child != None:
            print(node.value, "의 자식들")
            for childNode in node.child:
                print("value: ", childNode.value, "--depth: ", childNode.depth)
                queue.append(childNode)
        


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
    