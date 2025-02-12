# Write a program that take 10 number from user and count how many number are +ve and how many number are -ve.


num = 1
positive = 0
negative = 0
while num<=10:
    number = int(input("enter a number :"))
    if number>0:
        positive += 1
    else:
       negative += 1
    
    num += 1       
print("positive number",positive)
print("negitive number",negative)