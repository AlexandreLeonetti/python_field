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
    for i , it  in enumerate(iters):
        element = next(it, 1000) # must  add None in the next() method
        heapq.heappush(minHeap,(element, i))
    print(minHeap)

    #pass all values to minHeap and append them to result
    while minHeap:
        element, origin = heapq.heappop(minHeap)
        #print(element,origin)
        result.append(element)
        nxtElement = next(iters[origin], 1000) # 1000 is the default value returned by iterator
        # when the iterator is exhausted
        if nxtElement != 1000:
            heapq.heappush(minHeap,(nxtElement, origin))


    return  result


print(merge(arr1, arr2, arr3))

