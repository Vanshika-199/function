# a=list(input("enter the number"))
# while a[-1]==0:
#     a.pop(-1)
# print(a)

    

list1 = [9,6,0,0,0,0,0]
def pop_zeros(items):
    while items[-1] == 0:
        items.pop()
pop_zeros(list1)
print(list1)

#.Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
