a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    # print(e)
    # print("Sorry some error occurred")
    print("Invalid input!")

print("Some imp lines of code")
print("End of Program")


try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error")



try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")