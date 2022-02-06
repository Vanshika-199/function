#position of prime number

a=int(input("enter the number"))
def prime_number(a):
    count=0
    i=0
    while i<=a:
        f=0
        j=1
        while j<=i:
            if i%j==0:
                f=f+1
            j=j+1
        if f==2:
            x=i
            count=count+1
        i=i+1
    print(x)
prime_number(a)

#prime number

num = int(input("enter the number"))
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")  
else:
    print(num, "is not a prime number")



#Write a function to check if a number is prime or not.

