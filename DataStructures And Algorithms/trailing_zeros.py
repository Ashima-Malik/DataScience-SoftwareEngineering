# This method is the basic method but have the problem for bigger n values becuase of overflow

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

# print(factorial(1000))
def trailingzeros(n):
    value = factorial(n)
    val = str(value)
    count = 0
    for i in range(len(val)-1,-1,-1):

        if val[i] == '0' and val[i-1] == '0':
            count+=1
        elif val[i] == '0' and val[i-1] != '0':
            count+=1
            break
    return count

print(trailingzeros(100))

# This method is the optimized solution.
# trailing zeros of n = floor(n/5)+floor(n/25)+floor(n/125)

def trailingzeros(n):
    if n<0:
        return -1
    count = 0
    while n >= 5:
        n//=5
        count+=n
    return count

