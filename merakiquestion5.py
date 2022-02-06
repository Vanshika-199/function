#QUESTION 6(PART1)(CALCULATOR)


def calculator(number_x,number_y,operation):
    if operation==  "add":
        number_1=number_x+number_y
        return number_1
    elif operation==  "subtract":
        number_2=number_x-number_y
        return number_2
    elif operation==  "multiply":
        number_3=number_x*number_y
        return number_3
    elif operation==  "divide":
        number_4=number_x/number_y
        return number_4
number_x=int(input("enter the first number:  "))
number_y=int(input("enter the second number: "))
operation=input("enter the operation you want to do:  ")
print(calculator(number_x,number_y,operation ))

#QUESTION 6(PART2)


def a(m,n):
    return (m+n)
def b(m,n):
    return (m-n)
def c(m,n):
    return (m*n)
def d(m,n):
    return (m%n)
def e(m,n):
    return (m//n)
def f(m,n):
    return (m/n)
def name(num1,num2):
    g=a(num1,num2)
    h=b(num1,num2)
    i=c(num1,num2)
    j=d(num1,num2)
    k=e(num1,num2)
    l=f(num1,num2)
    return g,h,i,j,k,l
o=int(input("enter the first number"))
p=int(input("enter the second number"))
print(name(o,p))

#QUESTION 6(PART3)
      #IN FOR LOOP

def sum():
    a=[7,8,2,3]
    b=[4,5,6,7]
    product=[]
    for i in range(0,len(a)):
        product.append(a[i]*b[i])
    print(product)
sum()

#IN WHILE LOOP

a=[6,8,3,2]
b=[6,2,7,4]
i=0
n=[]
while i<len(a):
    n.append(a[i]*b[i])
    i=i+1
print(n)

 


    



