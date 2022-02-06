#first 10 natural numbers

def sum(n):
   if n <= 1:
       return n
   else:
       return n + sum(n-1)
num = int(input("enter the number: "))
if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",sum(num))

#first 10 whole numbers

def sum(n):
   if n <= 0:
       return n
   else:
       return n + sum(n-1)
num = int(input("enter the number: "))
if num <= 0:
   print("Enter a positive number")
else:
   print("The sum is",sum(num))


