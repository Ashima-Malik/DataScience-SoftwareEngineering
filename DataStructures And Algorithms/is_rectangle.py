def is_rectangle(A,B,C,D):
    _dict = {}
    if (A==B or A==C or A==D):
        _dict[A]=2
    if (B == C or B==D):
        _dict[B]=2
    if C==D:
        _dict[C]=2
    if len(_dict) == 2:
        return True
    return False

print(is_rectangle(1,2,3,4))



