#QUESTION 1

def employee(name,salary=20000):
    print(name,"your salary is:-",salary)
employee("kartik",30000)
employee("deepak")
# output:-
#     kartik your salary is:- 30000
#     deepak your salary is:- 20000

#QUESTION 2

def primeorNot(n): 
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                print(n,"is not a prime number")
                print(i,"times",n//i,"is",n)
                break
            else:
                print(n,"is a prime number")
    else:
        print(n,"is not a prime number")
primeorNot(406)
#output:-
    #406 is not a prime number
    #2 times 203 is 406

#QUESTION 3

from typing import SupportsRound


def greet(*names):
    for name in names:
        print("Hello", name)
greet("sonu", "kartik", "umesh", "bijender")
#output:-
    # Hello sonu 
    # Hello kartik
    # Hello umesh
    # Hello bijender

#QUESTION 4

def sumofdigits(number):
    sum = 0
    modulus = 0
    while number!=0 :
        modulus = number%10
        sum+=modulus
        number/=10
        return sum
print(sumofdigits(123))
#output:- 3

#QUESTION 5

def  meal(day,time):
    if day=="sunday":
        if time=="breakfast":
            return "dosa"
        elif time=="lunch":
            return "dal rice"
        elif time=="dinner":
            return "paneer and  chapati"
        else :
            return "time not found"
    elif day=="monday":
        if time=="breakfast":
            return "fried rice"
        elif time=="lunch":
            return "aloo rice"
        elif time=="dinner":
            return "chhole bhature"
        else :
            return "time not found"
    elif day=="other":
        if time=="breakfast":
            return "aloo"
        elif time=="lunch":
            return "rajma rice"
        elif time=="dinner":
            return "veg-chapati"
        else :
            return "time not found"
print(meal("sunday","lunch"))
print(meal("monday","dinner"))
#output:-
    #dal rice
    #chole bhature

#QUESTION 6

def checkKey():
    car ={"brand":"ford","model":"mustang","year":1964}
    if "model" in car:
        print("Yes, 'model' is one of the keys in the dictionary.")
    else:
        print("No, 'model' key dictionary mai nahi hai.")
checkKey()
#output:-
    #yes, 'model' is one of the keys in the dictionary





