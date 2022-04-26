######################2019B#############################


############Q3################

import random


def ranksearch(lst, k):
    return _helper(lst, 0, len(lst), k)


def _helper(lst, start, end, k):
    print('start= ', start)
    print('end= ', end)
    pivot_index = partition(lst, start, end)
    if pivot_index == k:
        return lst[pivot_index]
    elif pivot_index <= k:
        _helper(lst, pivot_index + 1, end, k)
    elif k <= pivot_index:
        pivot_index = partition(lst, start, end)
        _helper(lst, start, pivot_index, k)


def partition(data, start, end):
    pivot_ind = random.randrange(start, end)
    pivot_val = data[pivot_ind]
    data = data[:pivot_ind] + data[pivot_ind + 1:end] + [data[pivot_ind]]
    pivot_ind = end - 1
    end -= 1
    while start < end:
        print('start= ', start)
        print('end= ', end)
        print('data= ', data)
        if data[start] < pivot_ind:
            start += 1


        elif data[end - 1] >= pivot_ind:
            end -= 1
        else:
            data = data[:pivot_ind] + data[pivot_ind + 1:end] + [data[pivot_ind]]
            start == 1
            end -= 1
    data = data[:pivot_ind] + data[pivot_ind + 1:end] + [data[pivot_ind]]
    return start


def swap(data, pivot_ind, end):
    data = data[:pivot_ind] + data[pivot_ind + 1:end] + [data[pivot_ind]]
    return


###################################quick sort################################

def quick_sort(lst):
    return quick_sort_helper(lst, 0, len(lst))


def quick_sort_helper(lst: list, start, end):
    if start < end-1:
        pivot_index = sorting(lst, start, end)
        quick_sort_helper(lst, start, pivot_index)
        quick_sort_helper(lst, pivot_index-1, end)


def sorting(lst, start, end):
    pivot_index = random.randrange(start, end)
    pivot_val = lst[pivot_index]
    lst.append(lst.pop(pivot_index))
    pivot_index = end - 1
    end -= 1
    while start < end:
        if lst[start] < pivot_val:
            start += 1
        elif pivot_val <= lst[end-1]:
            end -= 1
        else:
            lst[start], lst[end-1] = lst[end-1], lst[start]
            start += 1
            end -= 1
    lst = lst[:start] + [lst.pop()] + lst[start:]
    return start + 1


########################merge sort#################

def marge_sort(lst):
    return helper(lst, 1, len(lst))


def helper(lst, start, end):
    if 1 < len(lst):
        mid = (start + end) // 2
        left = lst[:mid + 1]
        right = lst[mid + 1:]
        helper(left, 0, mid)
        helper(right, mid, end)
        r = l = k = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                lst[k] = left[l]
                l += 1
            elif right[r] < left[l]:
                lst[k] = right[r]
                r += 1
            k += 1
        while l < len(left):
            lst[k] = left[l]
            l += 1
            k += 1
        while r < len(right):
            lst[k] = right[r]
            r += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    quick_sort(arr)
    #marge_sort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

