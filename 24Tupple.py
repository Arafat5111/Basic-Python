tup = (1, 2, 76, 342, 32, "Green", True) # , is nessesury
# tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if 342 in tup:
    print("Yes 342 is present in this tuple")
else:
    print("Not present")
tup2 = tup[1:4]
print(tup2)
