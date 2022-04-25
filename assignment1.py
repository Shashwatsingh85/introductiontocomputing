'''
A = int(input("Enter the First Number:"))
B = int(input("Enter the Second Number:"))
C = int(input("Enter the Third Number:"))
Average = (A + B + C)/3 
print("The Average of these three numbers is :",Average)

GI = int(input("Enter the Gross Income :"))
Dep = int(input("Enter the Number of Dependents :"))
taxable_income= ( (GI - 10000) - Dep*3000 )
Tax= taxable_income*(0.2)
print(f"Your Tax is : {Tax}")

N = int(input("Enter seconds: "))

Mins = N // 60
Secs = N % 60

print(Mins, "Minutes and", Secs, "Seconds")

A = 25 
num = '25'
B = int(num) 
new = 25.0 
C = int(new)
D=A+B+C 
D=str(D)
print(D)
print(type(D))
'''
import math

for i in range(0,360,15):
    sin = round(math.sin(i*math.pi/180),4)
    cos = round(math.cos(i*math.pi/180),4)
    print(i,"---",sin,cos)
