#"""
#if condition:
    
#else conition:
#"""

#age = input("Enter age:")

#"""
#age=int(input("Enter age:"))
#print(age)


#if age > 18:
 #   print("your age is",age,"you are eligible for voting.")
#else :
#    print("your age is",age,"you are not eligible for voting.")

#ATM TASK

pin1 = 1234
pin2 = int(input("Enter your pin number:"))

if pin2 == pin1:
    act_type1= "savings"
    act_type2= int(input("Enter your account type:"))
    if act_type2 == act_type1:
        amount = int(input("Enter the amount to with  draw:"))
        print(amount,"is debited from your account.")
    else:
        print("account type doesnot match!")

else:
    print("pin does not match!")

