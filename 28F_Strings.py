# letter = "Hey my name is {1} and I am from {0}."
letter = "Hey my name is {} and I am from {}."
country = "Bangladesh"
name = "Arafat"

print(letter.format(name, country))
# print(letter.format(country, name))

print(f"Hey my name is {name} and I am from {country}")

# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49.09999))

price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())