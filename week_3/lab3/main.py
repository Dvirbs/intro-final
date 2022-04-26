def find_biggest(lst):
    maxi = lst[0][0]
    print(maxi)
    the_list = []
    for List in lst:
        for num in List:
            if maxi < num:
                maxi = num
                #                print(maxi)
                the_list = List
            else:
                return lst[0]
        print(the_list)
    return the_list

lst = [[999, -100], [1, 2, 3], [10, -2],  [1, 1, 1, 1]]
print(find_biggest(lst))
