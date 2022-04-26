###   2017 a2 ############


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left


def set_val(x, path, data):
    if len(path) == 0:
        x.data = data
        return
    elif x.left == None:
        if path[0] == 'L':
            x.left = BinaryTreeNode()
        else:
            x.right = BinaryTreeNode()

    nxt = x.left if path[0] == 'L' else x.right
    set_val(nxt, path[1:], data)


x = BinaryTreeNode(5, BinaryTreeNode(3, BinaryTreeNode(3), BinaryTreeNode(3)))
set_val(x, ['L', 'R'], 4)
print(x.left.right.data)




################################ sort
def sort(self):
    if len(self.stack) == 0 or len(self.stack) == 1:
        return
    else:
        for i, first in enumerate(self.stack):
            for sec in enumerate(self.stack):
                if first < sec:
                    self.stack[i], self.stack[j] = self.stack[j], self.stack[i]

