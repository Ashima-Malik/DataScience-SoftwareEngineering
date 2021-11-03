# def rev(str):
#     size = len(str)
#     if size==0:
#         return
#     else:
#         l = str[size-1]
#         print(l, end= " ")
#         rev(str[0:size-1])
#
# rev('1a4b5')

def rev(str):
    size = len(str)
    if size==0:
        return
    else:
        l = str[size-1]
        if l.isdigit():
            find(int(l))
            print(" ")
        rev(str[0:size - 1])
        # if l.isdigit():
        #     find(int(l))
        print()



def find(num):
    if num==0:
        return
    else:
        find(int(num/2))
        print(num%2, end=" ")

rev('1a4b5')
