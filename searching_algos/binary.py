#!/usr/local/bin/python3

def search(arr, el):
    ''' find element in array via binary search'''
    arr = sorted(arr)
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = (low + high) // 2
        if arr[mid] == el:
            return "Element Found"
        elif arr[mid] < el:
            low = mid + 1
        else:
            high = mid - 1
    return "Element Not Found"


if __name__ == '__main__':
    arr = [12, 3, 45, 56, 7, 43, 34]
    el = 100
    res = search(arr, el)
    print(res)
