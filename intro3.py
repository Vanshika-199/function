#QUESTION 1

def calculate_sum(a,b):
    sum = a+b
    print(sum)
calculate_sum(4,5)

#QUESTION 2

def function_multi(a,b):
    multiply=a*b
    return multiply
print(function_multi(3,4))

#QUESTION 3

def Avg(number1,number2,number3):
    avg=number1+number2+number3/3
    print(avg)
Avg(1,3,2)

#QUESTION 4

def voter(age):
    if age > 18:
        print("eligible")
    else:
        print("not eligible")
age=int(input("enter the age: "))
voter(age)

#QUESTION 5

def distance(kms):
    if kms < 20:
        print("close")
    elif kms < 50:
        print("median")
    else:
        print("far")
kms=int(input("enter the kms: "))
distance(kms)