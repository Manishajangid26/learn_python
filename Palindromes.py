def ispalindrome(data):
    data = str(data)
    if data [ ::-1 ] == data:
        return 1
    else:
        return 0

print(ispalindrome(2233))        
