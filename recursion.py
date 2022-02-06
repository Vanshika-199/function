#Introduction

def twopowers(number):
    if number==1:
        return 1
    return 2 * twopowers(number-1)
index=1
while(index<=10):
    print(twopowers(index))
    index+=1

# Simple series 1, 4, 7, 10, 13, 16.....

print("Enter the First Number:")
first_num=int(input())
print("Enter the range of number(Limit)")
n=int(input())
print("Enter the Difference Between two Number:")
diff=int(input())
while(first_num<=n):
     print(first_num,end=" ")
     first_num+=diff

#alternative series 2:- 10, 11, 110, 111, 1110, 1111, 11110, 11111, 111110, 111111 …

def pattern(number):
    if number == 1:
        return 10
    elif number % 2 == 0:
        return pattern(number - 1) + 1
    else:
        return pattern(number - 1) * 10
number=int(input("enter the number"))
print(pattern(number))

#factorial

def factorial(number):
    if number==1:
        return 1
    return number * factorial(number - 1)
number=int(input("enter the number"))
print (factorial(number))

#sum of a list

def sum_list(lis):
    if len(lis)==1:
        return lis[0]
    return lis[0] + sum_list(lis[1:])
print (sum_list([1, 4, 7, 10]))

#pallindrome string

def ifPalindrome(string):
    if string == "": 
        return True
    elif len(string) == 1:  
        return True
    elif string[0] == string[len(string)-1]:  
        return ifPalindrome(string[1:][:-1])
    else:
        return False
string=input("enter the string:  ")
print(ifPalindrome(string))

#fibonacci series

def getFibNumber(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return getFibNumber(number-1) + getFibNumber(number-2)
number=int(input("enter the number: "))
print(getFibNumber(number))

#fibonacci advance

def getFibList(number):
    if number == 1:
        return [1]
    elif number == 2:
        return [1, 1]
    else:
        get_previous_fib_list = getFibList(number-1)
        new_last_element = get_previous_fib_list[-1] + get_previous_fib_list[-2]
        get_previous_fib_list.append(new_last_element)
        current_fib_list = get_previous_fib_list
        return current_fib_list
number=int(input("enter the number"))
print(getFibList(number))

#binary search

def is_present_in_list(number_to_search, list_to_search):
    counter = 0
    while (counter < len(list_to_search)):
        if number_to_search == list_to_search[counter]:
            return True
        counter += 1
    return False
print (is_present_in_list(3, [3, 5, 7, 8, 4, 6, 2, 1, 9]))
print (is_present_in_list(10, [3, 5, 7, 8, 4, 6, 2, 1, 9]))

#calculate

def operate(num1, operator, num2):
    if operator=='+':
        return num1 + num2
    elif operator=='-':
        return num1 - num2
    elif operator=='*':
        return num1 * num2
    else:
        return num1 / num2
def solve(question_list):
    if len(question_list)==1:
        return int(question_list[0])
    elif len(question_list)==3:
        return operate(int(question_list[0]), question_list[1], int(question_list[2]))
    else:
        return operate(solve(question_list[:-2]), question_list[-2], int(question_list[-1])) 
question_list=list(input("enter the question list"))
print(solve(question_list))

#nested list

import types

def nested_to_flat(lis):
    flat_list = []
    index = 0
    while (index < len(lis)):
        element = lis[index]
        if type(element) != types.IntType:
            flat_list = flat_list + nested_to_flat(element)
        else:
            flat_list.append(element)
        index += 1
    return flat_list
lis=list(input("enter the list: "))
print(nested_to_flat(lis))





