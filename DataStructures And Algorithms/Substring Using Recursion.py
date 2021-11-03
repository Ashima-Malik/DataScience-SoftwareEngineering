def issubtring(str1, str2):
    size1 = len(str1)
    size2 = len(str2)
    if size1 == 0:
        return False
    if size2==0:
        return True
    if str1[0]==str2[0]:
        return exactsame(str1, str2)
    return issubtring(str1[1:], str2)

def exactsame(str1, str2):
    size1 = len(str1)
    size2 = len(str2)
    if size1 == 0:
        return False
    if size2 == 0:
        return True
    if str1[0]==str2[0]:
        return exactsame(str1[1:], str2[1:])
    return False

print(issubtring('NETSOTOS', 'SET'))