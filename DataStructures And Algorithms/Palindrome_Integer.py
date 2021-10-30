# Palindrome integer for the number ---->


def palindrome(A):
    # A = [i for i in A]
    # A = list(map(int, A))
    A = str(A)
    i = 0
    j = len(A)-1
    val = True
    while i <= j:
        if A[i] == A[j]:
            i+=1
            j-=1
            val = True
            # continue
        else:
            val = False
            return val
    return val
print(palindrome(2147447413))


# Palindrome integer for the number ---->

num = 1223
# print(str(num))
res =  str(num) == str(num)[::-1]
# print(res)


