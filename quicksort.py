
def hoare_partition(A, p, r):
    pivot = A[p]
    i = p - 1
    j = r + 1
    while True:
        while True:
            j -= 1
            if A[j] <= pivot:
                break
        while True:
            i += 1
            if A[i] >= pivot:
                break
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j
            
def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)
    
def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q - 1)
        randomized_quicksort(A, q + 1, r)

def partition(A, p, r):
    pivot = A[r]
    
    # start index i 
    # one before the primary index
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]        
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)
    
