# def avarage(a=9, b=1):

#     print("The Avarage is ", (a+b)/2)

# avarage(b=5)
# avarage(1, 5)

# def name(fname, mname = "Hossain", lname = "Chowdhory"):
#     print("Hello,", fname, mname, lname)
# name("Arafat")
# avarage(a=21)

def avarage(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Avarage is: ", sum / len(numbers)) 
    # return 7
    return sum / len(numbers) 

c = avarage(5, 6, 25) 
print(c)

# def name(**name):
#     # print(type(name))
#     print("Hello,", name["fname"], name["mname"], name["lname"])

#     name(mname = "Arafat", lname = "Alvee", fname = "Jahid")
