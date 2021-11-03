def hammingDistance(A):
    ans = 0  # Initialize result

    # traverse over all bits
    for i in range(0, 32):

        # count number of elements with i'th bit set
        count = 0
        for j in range(0, len(A)):
            if ((A[j] & (1 << i))):
                count += 1

        # Add "count * (n - count) * 2" to the answer
        ans += (count * (len(A) - count) * 2);

    return ans
print(hammingDistance([2,4,6]))
