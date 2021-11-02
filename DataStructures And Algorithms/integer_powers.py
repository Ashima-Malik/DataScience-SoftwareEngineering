
import math

def isPower(n):

    if (n <= 1):
        return True
    for x in range(2, (int)(math.sqrt(n)) + 1):
        p = x
        while (p <= n):
            p = p * x
            if (p == n):
                return True

    return False

print(isPower(49))