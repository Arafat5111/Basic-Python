    # Loop over a list and print the index and value of each element
# fruits = ['apple', 'banana', 'mango']
# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# marks = [12, 56, 32, 98, 12, 45, 1, 4]
# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Arafat, Awesome!")

#     index +=1

marks = [12, 56, 32, 98, 12, 45, 1, 4]

for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("Arafat, Awesome!")

    index +=1

# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(index, color)

# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)
