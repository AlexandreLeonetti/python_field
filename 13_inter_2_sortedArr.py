# intersection of two sorted array

# if both arrays differs significantly,
# we could loop linearly through the first array
# then use binary search into the big array for each element.

def intersect(arr1, arr2):
    intersection  = []
    previous_a = None
    
    for i, a in enumerate(arr1):
        print(i, a, previous_a)
        if i == 0 or a != previous_a:
            if a in B: # perform binary search here 
                intersection.append(a)
        previous_a = a

    return intersection





