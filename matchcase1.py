# write a program that take input from user and display it's subsequent week day.
# Example:
# 1 it will show monday,
# 2 it will show Tue

num = int(input("enter 1 to 7 number"))

match num:

   case 1:
      print("monday")

   case 2:
      print("tue")

   case 3:
      print("wed")

   case 4:
      print("thur")

   case 5:
      print("fri")

   case 6:
      print("sat")

   case 7:
      print("sun")

   case _ :
      print("press only 1 to 7")