def find(num):
    if num==0:
        return
    else:
        find(int(num/2))
        print(num%2, end=" ")

print(find(9))