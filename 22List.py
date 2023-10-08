marks = [3, 5, 6, "Arafat", True, 6, 7, 2, 32, 345, 23]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Nagative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

# if 6 in marks:
#     print("Yes")
# else:
#     print("No")

         #smae things applies for string as well
# if "fat" in "Arafat" :
#     print("Yes")

# print(marks)
# print(marks[1:8])
# print(marks[1:8:3])

lst = [i*i for i in range(10)]
print(lst)

lst = [i*i for i in range(10) if i%2==0]
print(lst)