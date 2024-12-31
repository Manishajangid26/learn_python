a = input("enter a string :")
i = 0

while i <= len(a):
    print(a[i])
    if a[i] in ('a','e','i','o','u' , 'A','E','I','O','U'):
        print("vowel")

    else:
        print("consonant")   
    i += 1 
