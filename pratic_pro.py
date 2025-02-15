def no_boring_zeros(n):
    if n == 0:
        return 0
    return int(str(n).rstrip('0'))
    # number = int("enter number")


result = no_boring_zeros(0)
print(result)


