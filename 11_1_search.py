# search for first occurrence of k in a sorted array
# using binary search

def bin_search(arr, t):
    left = 0
    right=len(arr)-1
    index = 0
    mid = 0
    while left <= right :
        mid= (left + right)//2
        #search
        # if t bigger than middle, then left becomes middle
        if t>arr[mid]:
            left = mid+1
        # if t smaller than middle then right becomes middle
        elif t == arr[mid]:
            index = mid
            right= mid-1 # continue the search to the left 
        else:# t<arr[mid]:
            right = mid-1
    return index 




# Test case
sorted_array = [1, 2, 2, 3, 4,4, 5, 5, 5, 6, 7, 8, 9]
target = 5
print(bin_search(sorted_array, target))



