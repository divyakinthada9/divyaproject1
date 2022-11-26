pin1 = 1986
pin1 = int(input("Enter your pin number"))
print(type(pin1))
if pin1 == 1986:
    print("your pin number is",pin1,"your pin number is correct.")

else :
    print("your pin number is",pin1,"youe pin number is incorrect.")

print(pin1)

act_type1 = "savings"
act_type1 = str(input("Please Enter your account type"))
print(type(act_type1))
if act_type1 == "savings":
    print("your account type is",act_type1,"your account type is correct.")

else:
    print("your account type is",act_type1,"your account type is incorrect.")

print(act_type1)

act_balance = 5000
act_balance = int(input("Current  balance in your account"))
print(type(act_balance))

if act_balance == 5000 :
    print("Current balance in your account is",act_balance,"Enter your amount to withdrawl.")

else : 
    print ("Current balance in your account is",act_balance,"Insufficent balance your account.")

print(act_balance)
