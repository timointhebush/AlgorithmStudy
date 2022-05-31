class Node:
    def __init__(self, value, x):
        self.value = value
        self.x = x
        self.left, self.right = None, None


class Tree:
    def __init__(self, root):
        self.root = root

    def _insert(self, parent_node, value, x):
        is_right = False
        if parent_node.x < x:
            target_node = parent_node.right
            is_right = True
        else:
            target_node = parent_node.left

        if target_node is None:
            target_node = Node(value, x)
            if is_right:
                parent_node.right = target_node
            else:
                parent_node.left = target_node
        else:
            self._insert(target_node, value, x)

    def insert(self, value, x):
        self._insert(self.root, value, x)

    def _preorder(self, parent_node, value_list):
        value_list.append(parent_node.value)
        if parent_node.left is not None:
            self._preorder(parent_node.left, value_list)
        if parent_node.right is not None:
            self._preorder(parent_node.right, value_list)
        self.preorder_result = value_list

    def preorder(self):
        self._preorder(self.root, [])
        return self.preorder_result

    def _postorder(self, parent_node, value_list):
        if parent_node.left is not None:
            self._postorder(parent_node.left, value_list)
        if parent_node.right is not None:
            self._postorder(parent_node.right, value_list)
        value_list.append(parent_node.value)
        self.postorder_result = value_list

    def postorder(self):
        self._postorder(self.root, [])
        return self.postorder_result


def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i] = [i + 1, nodeinfo[i]]
    nodeinfo = sorted(nodeinfo, key=lambda x: -x[1][1])

    tree = Tree(Node(nodeinfo[0][0], nodeinfo[0][1][0]))
    for i in range(1, len(nodeinfo)):
        value, x = nodeinfo[i][0], nodeinfo[i][1][0]
        tree.insert(value, x)
    return [tree.preorder(), tree.postorder()]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))