# write a program to calculate the salary of a sales person based on the bonus and incentiv to 
# be offered him based on the sale they made . 
# if the sale exceeds Rs. 100000 then follow table 1 else follow table 2
# table1:
# basic = 3000
# hra = 20% of basic
# da  = 110% of basic
# converyance = 500
# incentiv = 10% of sales
# bonus = 500 

# table2:
# basic = 3000
# hra = 20% of basic
# da  = 110% of basic
# converyance = 500
# incentiv = 5% of sales
# bonus = 500 

sale = int(input("enter your sales:"))
basic = 3000
hra = (basic*20)/100
da = (basic*110)/100
converyance = 500
bonus = 500
if sale>100000:
    incentiv = sale*10/100
else:
    incentiv = sale*5/100
total = basic + hra + da + converyance + incentiv  
print(total)      