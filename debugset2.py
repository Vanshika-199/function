#QUESTION 1

def greet(names):
    for name in names:
        print("Welcome", name)
greet("Zoya")

#QUESTION 2

def info(name, age ="20"):
    print(name + " is " + age + " years old")

info("Sonu")
info("Sana", "17")
info("Umesh", "18")

#QUESTION 3

def studentDetails(name,currentMilestone,mentorName):
    print("Hello ",name,"your",currentMilestone,"concept","is clear with the help of",mentorName)
studentDetails("Nilam","loop","Vanshika")