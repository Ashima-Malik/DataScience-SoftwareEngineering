## Naive solution
# def threeSum(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[List[int]]
#     """
#     l = []
#     n = len(nums)
#     nums = sorted(nums)
#     for i in range(n - 2):
#         for j in range(i + 1, n - 1):
#             for k in range(j + 1, n):
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     lst = [nums[i], nums[j], nums[k]]
#                     l.append(lst)
#     # (list(map(list, set(map(tuple, l)))))
#
#     return (list(map(list, set(map(tuple, l)))))
#
# print(threeSum([-1,0,1,2,-1,-4]))

def threesums(A):
    A = sorted(A)
    # k = len(A)-1
    l = []
    for i in range(0, len(A)-2):
        j = i+1
        k = len(A) - 1
        while j < k:
            _sum = A[i]+A[j]+A[k]
            if _sum==0:
                if [A[i],A[j],A[k]] not in l:
                    l.append([A[i], A[j], A[k]])
                j+=1
                k-=1
            elif _sum < 0:
                j+=1
            elif _sum > 0:
                k-=1
    return l
print(threesums([-4,-1,-1,0,1,2]))


