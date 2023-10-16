# let'ts try to merge several arrays 
# the arrays are sorted so we need to use iterators.
import heapq


arr1 = [0,0,0,1,3,5,7,9]
arr2 = [4,5,6,7,8,9,11,12,13]
arr3 = [55,56,57,578]

def merge(*args):
    allArrs = args
    result = []
    minHeap =[]
    # instantiate an iterator for each array
    iters = [iter(x) for x in allArrs ]
   
    for i,it in enumerate(iters):
        firstElt = next(it, None)
        if firstElt is not None:
            heapq.heappush(minHeap, (firstElt, i))
    
    # push pop and append from the minHeap
    while minHeap:
        smallestEntry, smallestOrigin = heapq.heappop(minHeap)
        result.append(smallestEntry)
    
        smallestIter = iters[smallestOrigin]
        nxtElt = next(smallestIter, None) #check what is the None in the next method
        if nxtElt is not None:
            heapq.heappush(minHeap, (nxtElt,smallestOrigin))



    return result 


print(merge(arr1,arr2,arr3))


