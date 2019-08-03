class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node:{self.val}"

    __repr__ = __str__


class Tree:
    def __init__(self, root):
        self.root = root

    @classmethod
    def build_tree_from_array(cls, array):
        # array BFS

        lens = len(array)
        node_list = [Node(val) for val in array]
        t = cls(node_list[0])
        for idx, node in enumerate(node_list):
            left_idx = 2 * idx + 1
            right_idx = 2 * idx + 2
            if left_idx < lens:
                node.left = node_list[left_idx]
            if right_idx < lens:
                node.right = node_list[right_idx]
        return t

    def bfs(self):
        queue = [self.root]
        res = []
        while queue:
            cur = queue.pop(0)
            res.append(cur.val)
            cur.left and queue.append(cur.left)
            cur.right and queue.append(cur.right)
        return res
