#!/usr/local/bin/python3

def search(arr, el, low, high):
    ''' find element in array via binary search using recursion'''
    if low > high:
        return "Element Not Found"
    else:
        mid = (low + high) // 2
        if el == arr[mid]:
            return "Element Found"
        elif el < arr[mid]:
            return search(arr, el, low, mid - 1)
        else:
            return search(arr, el, mid + 1, high)


if __name__ == '__main__':
    arr = [12, 3, 45, 56, 7, 43, 34]
    arr.sort()
    el = 56
    res = search(arr, el, 0, (len(arr) - 1))
    print(res)
