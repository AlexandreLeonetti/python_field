# merge several aray using iterators

import heapq


a1 = [2,3,4,6,9,13,21]
a2 = [1,1,1,2,3,4,5,7]
a3 = [8,9,12,34,45,67,99]

def mixer (*args):
    arrs = args 
    minheap = []
    result = []
    arrOfIters = [iter(x) for x in arrs ] 
    
    # initialize iterators

    for i, it in enumerate(arrOfIters):
        firstElt = next(it, None)
        if firstElt is not None:
            heapq.heappush(minheap, (firstElt, i))

        print("min heap", minheap)


    # push pop and append from min heap and out into arrs result
    while minheap :
        #print("min heap  whilej")
        smallestEntry, smallestEntryOrigin = heapq.heappop(minheap)
        result.append(smallestEntry)
        smallest_array_iter = arrOfIters[smallestEntryOrigin]

        nxtElt = next(smallest_array_iter, None)
        if nxtElt is not None:
            heapq.heappush(minheap, (nxtElt, smallestEntryOrigin))



    return result 




print(mixer(a1,a2,a3))
