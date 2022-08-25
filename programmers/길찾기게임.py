class Node:
    def __init__(self, value, x):
        self.value = value
        self.x = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = Node(None, -1)
        self.order_list = []

    def insert_node(self, value, x):
        self._insert_node(self.root, value, x)

    def _insert_node(self, node, value, x):
        if node.value is None:
            node.value = value
            node.x = x
            node.left = Node(None, -1)
            node.right = Node(None, -1)
        elif node.x < x:
            self._insert_node(node.right, value, x)
        else:
            self._insert_node(node.left, value, x)

    def preorder(self):
        self.order_list = []
        self._preorder(self.root)
        return self.order_list

    def _preorder(self, node):
        if node.value is not None:
            self.order_list.append(node.value)
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self):
        self.order_list = []
        self._postorder(self.root)
        return self.order_list

    def _postorder(self, node):
        if node.value is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            self.order_list.append(node.value)


def solution(nodeinfo):
    answer = []
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    nodeinfo = sorted(nodeinfo, key=lambda x: -x[1])
    tree = Tree()
    for (x, y, i) in nodeinfo:
        tree.insert_node(i, x)
    answer.append(tree.preorder())
    answer.append(tree.postorder())
    return answer


if __name__ == "__main__":
    print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))