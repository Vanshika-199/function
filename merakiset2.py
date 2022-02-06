#QUESTION 2

def function_print_lines():
    print("Mera naam Rishabh hai")
    print("Mai nbavgurukul ka co founder hun")
function_print_lines()

#QUESTION 3(PART1)

def student(*names):
    for name in names:
        print(name)
student("megha","vanshika","shekhar","mallilka")

#QUESTION 3(PART2)

def isGreaterthan20(b,a="20"):
    print(a,"is greater than",b,"or not?")
isGreaterthan20("77")
isGreaterthan20("40","60")

#QUESTION 4(PART1)

def add_numbers(number1,number2):
    print(number1+number2)
add_numbers(22,34)

#QUESTION 4(PART2)

def add_number_list():
    a=[10,20,30]
    b=[20,50,40]
    print(sum(a),"is the sum of a")
    print(sum(b),"is the sum of b")
add_number_list()

#QUESTION 5(PART1)

def check_numbers(firstnumber,secondnumber):
    if firstnumber%2==0 and secondnumber%2==0:
        print("dono numbers even hai")
    else:
        print("dono numbers even nahi hai")
check_numbers(45,50)

#QUESTION 5(PART2)

def check_number_list(a,b):
    i=0
    while i<len(a):
        j=0
        while j<len(b):
            if a[i]%2==0 and b[j]%2==0:
                print("dono even hain")
            else:
                print("dono even nahi hai")
            j+=1
        i+=1
check_number_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])
        