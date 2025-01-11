#     1
#    121
#   12321
#  1234321
# 123454321 

# 1
# 21
# 321
# 4321
i = 1
while i <= 5:
    print(" " * (5-i),end="")

    j = 1
    while j <= i:
        print(j,end="")
        j += 1


    j = i - 1 
    while j >= 1:
        print(j,end="")
        j -= 1   

    print()
    i +=1    
