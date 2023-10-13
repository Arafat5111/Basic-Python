fruits = ["Apple", "Orange", "Pineapple", "Grape"]
# Lets make juice with these fruits

start_index = 0
max_index = len(fruits) - 1

while start_index <= max_index: # Work until this condition is True
    fruit = fruits[start_index]
    print(fruit + " Juice!")

    start_index = start_index + 1


fruits = ["Apple", "Orange", "Pineapple", "Grape"]
# Lets make juice with these fruits

for fruit in fruits:
    print(fruit + " Juice!")



for i in range(10):
    print(i)
print("Done")


# start with 5 and ends with 10
for i in range(5, 10):
      print(i)
print("Okay")


# start with 5 and ends with 15 and step size 3
for i in range(5, 15, 3):
      print(i)
print("Okay")

# start with 10
# end with 0
# step size -2
for i in range(10, 0, -2):
     print(i)
print("Done")


# we need all of those three argumet, such as  start, stop, step
def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step
for i in frange(0.5, 1.0 ,0.1):
         print(i)
print("Thanks")


for letter in 'Python': # Here "Python" acts like a list of characters
    print(letter)
print("String")


for i in range(20):
    if i == 5:
        continue
    if i > 9:
        break
    print(i)

print("Printed first 10 numbers except 5!")


