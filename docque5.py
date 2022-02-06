a=[1,2,3,3,3,3,4,5]
def duplicates(a):
    i=0
    b=[]
    while i<len(a):
        if i in a:
            if i not in b:
                b.append(i)
        i=i+1
    print(b)
duplicates(a)

#Write a Python function that takes a list and returns a new list with unique elements of the first list.
