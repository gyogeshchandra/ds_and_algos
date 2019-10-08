#!/usr/local/bin/python3

def search(arr, el):
    '''find element in array via linear search'''
    for i in arr:
        if i == el:
            return "Element found"
    return "Element Not Found"


if __name__ == '__main__':
    arr = [11, 43, 23, 32, 26, 10, 12]
    el = 43
    res = search(arr, el)
    # ## pythonic way ##
    # res = 'Element found' if len(list(filter(lambda x: x == el, arr))) > 0 else "Element Not Found"
    print(res)

