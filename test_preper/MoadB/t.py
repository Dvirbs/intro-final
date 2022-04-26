class WordIter:
    def __init__(self, word):
        self.word = word
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i + 1 < len(self.word) and cur != ' ':
            cur = self.word[self.i]
            self.i += 1
            if cur != ' ':
                # print('cur=', cur)
                return cur
        else:
            raise StopIteration()


def get_iter1(word):
    return WordIter(word)


print(list(get_iter1(" h e l    l o     *")))

# for char in get_iter1(" h e l    l o     *"):
#     print(char, end="")
# print()
