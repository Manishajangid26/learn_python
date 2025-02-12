# 6. Write a program that take 10 number from user and display which is the largest number and which one is the lowest.

i = 0
largest = int(input("enter no"))
lowest = 0
num = print("enter 10 number :")
while (i<=5):
    if (num>largest):
        largest = num
    if(num<lowest):
       lowest = num
    i=i+1 
print("largest no :",largest)
print("lowerst no :",largest)           
   


# i = 0
# sm = print("enter 10 number :")
# while i<=10:
#     n = int(input())
#     if i ==1:
#         sm = n
#     elif n<sm:
#         sm = n    
#     i = i+1
# print("smalist number =",sm)    