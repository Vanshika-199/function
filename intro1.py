#QUESTION 1

def eligibleforvote(age):
    if age>=18:
        print("Eligible for voting")
    else:
        print("Not eligible to give vote")
age=int(input("Enter the age:" ))
eligibleforvote(age)

#QUESTION 2

def perfect():
    n = int(input("Enter any number: "))
    sum1 = 0
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    if (sum1 == n):
        print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")
perfect()

#QUESTION 3

def three(num1,num2,num3):
    a=num1+num2+num3
    b=num1+num2+num3/3
    return a, b
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
print(three(num1,num2,num3))

#QUESTION 4

def shownumber(limit):
    start=0
    num=start
    while num<limit+1:
        if num%2!=0:
            print(num,"ODD")
        else:
            print(num,"EVEN")
        num=num+1
limit=int(input("enter the limit"))
shownumber(limit)

#QUESTION 5

start=1
end=int(input("enter the limit"))
sum=0
num=start
while num<end+1:
    if num%3==0 or num%5==0:
        print(num)
    num=num+1
    sum=sum+num
print(sum,"is the total sum")

#QUESTION 6

def main(speed):
    point=1
    km=5
    if speed<=70:
        print("ok")
    elif speed>70:
        speed=speed-70
        point=int(1*speed/5)
        print(point,"is your point")
        if point>12:
            print("your license is suspended")
speed=int(input("enter the speed: "))
main(speed)

#QUESTION 7

def string(a,b):
    if len(a)==len(b):
        print(a,b)
    elif len(a)>len(b):
        print(a)
    else:
        print(b)
a=input("enter the first string: ")
b=input("enter the second string: ")
string(a,b)

#QUESTION 8(related to dictionary)

    

    
