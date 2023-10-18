# this program is supposed to merge two arrays using heaps
import heapq

arr1 = [0,0,0,1,2,3,4,5,6,7]
arr2 = [2,3,4,6,8,10,12,14,16]
arr3 = [100,222,333,444,555,666,777]


def merge(*args):
    all_arrs = args
    minHeap = []
    result = []

    # initialize array of iterator values
    iters = [iter(x) for x in all_arrs]

    #initialize minHeap

    #pass all values to minHeap and append them to result


    return  result


print(merge(arr1, arr2, arr3))

