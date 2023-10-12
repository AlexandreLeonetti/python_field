# Dutch flag problem
# in this problem we are going to sort 

arr = [1,2,0,2,2,2,1,1,0,0,2,1,0,2,1]
print(arr)

def dutch(A,p):
    # sort elements that are smaller than p
    for i in range(len(A)):
        for j in range(i,len(A)):
            if A[j]< p:
                A[j], A[i] = A[i], A[j]
                break
    # sort elements that are bigger than p
    for i in reversed(range(len(A))):
        for j in range(i):
            if A[j] > p:
                 A[j], A[i] = A[i], A[j]
               


dutch(arr,1)
print(arr)

