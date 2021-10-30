# Method 1 but not for overflow:

A = -1234567891
B = str(A)
if A < 0:
    B = '-'+''.join(list(reversed(B[1:])))
else:
    B = ''.join(list(reversed(B)))
print(B)

# Method 2 for overflow:
def reverse(A):
    neg = A < 0
    res = 0
    A = abs(A)
    while A > 0:
        a = A%10
        res = res*10 +a
        A = A//10
    if res > 1<<31:
        return 0
    if neg:
        return 0 -res
    else:
        return res

print(reverse(-123))
