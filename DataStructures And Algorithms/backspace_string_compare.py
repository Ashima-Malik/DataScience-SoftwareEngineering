def backspaceCompare(s):
    low=0
    high = len(s)-1
    while low <= high and len(s)>=2:
        mid = (low+high)//2
        if s[mid] == '#' and s[mid-1] != '#':
            s=s[mid+1:]
        elif s[mid]!= '#':
            low = low+1
            high = high-1
            s = s[low:high+1]
        elif s[high]=='#':
            s = s[:high-2]
        elif s[low] == '#':
            s = s[low+1:]
    return len(s)



print(backspaceCompare("abc#"))