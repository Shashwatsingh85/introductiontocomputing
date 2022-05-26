#ASSIGNMENT 4
#NAME : Shashwat Singh
#SID 21107090
#BRANCH: MECHANICAL
print("Q1")
a=int(input("enter marks: "))
# enter marks between 0-100
if a>=80 :
   print ("A")
elif a>=60 :
    print ("B")
elif a>=50 :
    print ("C")
elif a>=45 :
    print ("D")
elif a>=25 :
    print ("E")    
else :
    print ("F")

print("Q2")
Y=int(input("enter the Year " ))
#enter your year here 
'''now if the year is a leap year if it is divisible by 4, except that year is  divisible by 100 are not
leap years unless they are also divisible by 400. example 1700 '''
if Y%400 ==0:
    print ("it's a leap year")
elif Y%100 ==0 :
    print ("it is not a leap year")
elif Y%4 ==0 :
    print ("it is a leap year")
else :
    print ("it is not a leap year")    

print("Q3")
import random

for i in range(1,11):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    ans = int(input(f"Question {i}:{a}x{b}="))
    if ans == a*b:
        print("Right!")
    else:
        print('Wrong. The correct answer is', a*b)

print("Q4")
for i in range(200):
    if i % 5 == 2 and i % 6 == 3 and i % 7 == 2:
        print("Answer:",i)
            