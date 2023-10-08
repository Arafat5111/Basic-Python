# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia")       #add item 
# temp.pop(3)                 #remove item
# temp[2] = "Finland"         #change item
# countries = tuple(temp)
# print(countries)

# countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
# countries2 = ("Vietnam", "India", "China")
# southEastAsia = countries + countries2
# print(southEastAsia)

Tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = Tuple1.count(3)
# res = Tuple1.index(3)
# res = Tuple1.index(311)
# res = Tuple1.index(3, 4, 8)
res = len(Tuple1)
print('Count of 3 in Tuple1 is:', res)