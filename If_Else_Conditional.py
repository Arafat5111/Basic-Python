a = int(input("Enter your age"))
print("Your age is:", a)
# Conditional operator
# >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

if(a>18):
    print("You can Drive")
else:
    print("You cannot Drive")
    print("no")
    print("Arafat")

applePrice = 10
budget = 200
if(budget - applePrice > 50):
    print("Alexa, add 1kg Apple to the cart.")
elif(budget - applePrice > 70):
    print("Its okay you can buy")
else:
    print("Alexa do not add.")