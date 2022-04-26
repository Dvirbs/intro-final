class Tree:
    def __init__(self, value, branches=[]):
        self.value = value
        self.branches = list(branches)


def bfs_order(tree):
    def single_level_gen(tree, n):
        if n == 0:
            yield tree.value
        else:
            for children in tree.branches:
                yield from single_level_gen(children, n - 1)

    counter = 1
    n = 0
    while counter:
        counter = 0
        for branch in single_level_gen(tree, n - 1):
            counter += 1
            yield branch
        n +=1


branches = [Tree(4), Tree(3), Tree(1)]
tree = Tree(2, branches)
print(list(bfs_order(tree)))
