if 10 > 5:
    print("10 greater than 5") # এই স্টেটমেন্টটি if কন্ডিশনের এর আওতাভুক্ত
    print("IF scope finished")    # এই স্টেটমেন্টটিও if কন্ডিশনের এর আওতাভুক্ত

print("Program ended") # এই স্টেটমেন্টটি if কন্ডিশনের এর আওতাভুক্ত নয়


num = 12
if num > 5:
    print("Bigger than 5")
    if num <= 47:
        print("Between 6 and 47")

x = 4
if x == 5:
    print("Its 5")
else:
    print("Its not 5")


num = 7
if num == 5:
    print("Number is 5")
elif num == 11:
    print("Number is 11")
elif num == 7:
    print("Number is 7")
else:
    print("Number isn't 5, 11 or 7")



a = 100
b = 200 if (a >= 100 and a < 200) else 300
print(b)


status  = 1
msg = "Logout" if status == 1 else "Login"
print(msg)

for i in range(10):
    print(i)
else:
    print("Done")