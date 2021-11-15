# If the array is sorted

def two_sum(A, target):
    i = 0
    j = len(A)-1
    while i<=j:
        if A[i]+A[j]==target:
            return [i,j]
        elif A[i]+A[j]>target:
                j-=1
        else:
            i+=1
    return -1

print(two_sum([2,3,4],6))

## If array is not sorted
def two_sum(A, target):
    _dict = {}
    for i in range(len(A)):
        s = target-A[i]
        if s in _dict:
            return [_dict[s], i]
        else:
            _dict[A[i]]=i

print(two_sum([3,2,4],6))