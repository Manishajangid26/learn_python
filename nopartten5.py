# write a program to print following output.
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


i = 1

while i <= 5:

    j = 1
    while j <= i:
        print( j , end=" " )
        j += 1

    print()
    i += 1

