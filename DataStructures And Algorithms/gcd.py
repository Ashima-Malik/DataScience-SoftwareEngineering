def gcd(A, B):
		val = 0
		min_ = min(A, B)

		for i in range(1,min_+1):
			if A%i == 0 and B%i ==0:
				val = i




		return max(A,B) if min_ == 0 else val

# print(gcd(1,0))


# Method 2-

def gcd(A,B):
    if B > A:
        A,B= B,A
    while B!=0:
        temp = B
        B = A%B
        A = temp
    return A

print(gcd(1,0))