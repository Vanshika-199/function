#QUESTION 1

def divisible(n):
    i=0
    while i<=n:
        print(i)
        i=i+1
        if i%21==0:
            print("Navgurukul")
        elif i%3==0:
            print("Nav")
        elif i%7==0:
            print("Gurukul")
n=int(input("enter the number"))
divisible(n)

#QUESTION 2

def monthlycalculation(total_students,name,expenses):
    if expenses<=50000:
        print("Its under budget")
    else:
        print("Out of budget")
total_students=int(input("enter the total no.of students"))
name=input("enter the name")
expenses=int(input("enter the expenses of the student"))
monthlycalculation(total_students,name,expenses)

#QUESTION 3

def strongpassword(password):
    if len(password)<=6 or len(password)>=16:
        if "$" in password:
            if "2" in password or "8" in password:
                if "A" in password or "Z" in password:
                    print("Its a strong password")
                else:
                    print("Not a strong password")
            else:
                print("It must consist of 2 or 8 in it")
        else:
            print("Must contain a $ sign in it")
    else:
        print("Please check the length")
password=input("enter your password: ")
strongpassword(password)

#QUESTION 4

def maximum(a,b,c):
    if a>b and a>c:
        print("a is the largest of all")
    elif b>a and b>c:
        print("b is the largest of all")
    else:
        print("c is the largest of all")
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))
maximum(a,b,c)

#QUESTION 5

def factorial(num):
    i=1
    fact=1
    while i<=num:
        fact=fact*i
        i=i+1
    print(fact)
num=int(input("enter the number: "))
factorial(num)

#QUESTION 6

def duplicate(string_list):
    new=[]
    for i in string_list:
        if i not in new:
            new.append(i)
    print(new)
string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
duplicate(string_list)

#QUESTION 7

def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    print(result)
list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
common_elements(list1,list2)

#QUESTION 8

def common(list1,list2):
    list1.extend(list2)
    list=[]
    for i in list1:
        if i not in list:
            list.append(i)
    print(list)
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
common(list1,list2)

#QUESTION 9

def harshadnumber():
    a=int(input("enter the number"))
    b=a
    sum=0
    while b>0:
        c=b%10
        sum=sum+c
        b=int(b//10)
    if a%sum==0:
        print("harshad number")
    else:
        print("not a harshad number")
harshadnumber()

#QUESTION 10


def max_marks(marks):
    for i in marks:
        print(max(i))
marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
max_marks(marks)

#QUESTION 11

def break_into_words(words):
    x=str(words).split()
    print(x)
words = ["NavGurukul is an alternative to higher education reducing the barriers of current formal education system"]
break_into_words(words)