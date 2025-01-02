# 4. Write a program that take 10 number from user and display which is the largest number.

i = 0
largest = 0
while i<10:
    num = int(input("enter a number :"))
    if(num>i):
        largest = num
    i +=1
    print("The largest no is :",largest)

