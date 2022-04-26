def num_different_permutations(word):
    dic = {}
    for letter in word:
        if letter not in dic:
            dic[letter] = 1
        else:
            dic[letter] += 1
    return num_different_permutations_helper(dic)


def update(dic, letter):
    dic[letter] -= 1
    return dic


def num_different_permutations_helper(dic):
    origen_dic = {key: value for key, value in dic.items()}
    if sum(dic.values()) == 0:
        return 1
    count = 0
    for key in dic:
        if dic[key] >= 1:
            count += num_different_permutations_helper(update(dic, key))
        dic = origen_dic
    return count


print(num_different_permutations("aaabbbccc"))
