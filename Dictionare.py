my_marks = {"Bengali": 80, "English": 85, "Math": 90}
print(my_marks["Math"])


my_marks = {"Bengali" : [30, 35, 32], "English" : [45, 52, 33], "Math": [60, 74, 58]}
print(my_marks["Math"])

my_list = [2, 4, 6, 7]
my_list[3] = 8

print(my_list)

my_nums = {1 : 1, 2 : 4, 3 : 9, 4 : "What?"}
my_nums[4] = 16

print(my_nums)


my_nums = {1 : 1, 2 : 4, 3 : 9, 4 : 16}
my_nums[5] = 25

print(my_nums)


nums = {1: "one", 2: "two", 3: "three",}

print(1 in nums)
print("three" in nums)
print(4 not in nums)

my_nums = {1 : 1, 2 : 4, 3 : 9, 4 : 16}
print(my_nums.get(5))

my_nums = {1 : 1, 2 : 4, 3 : 9, 4 : 16}
print(my_nums.get(5, "5 not in my numbers!"))